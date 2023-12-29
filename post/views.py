from django.db import models
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Post, UserRating
from post.serializers import UserRatingSerializer, PostSerializer


class RatePostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRatingSerializer
    permission_classes = [IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        post_id = kwargs.get("post_id")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        rating = serializer.validated_data.get('rating')

        post = Post.objects.get(pk=post_id)
        user_rating, created = UserRating.objects.get_or_create(user=user, post=post)
        user_rating.rating = rating
        user_rating.save()

        ratings = UserRating.objects.filter(post=post)
        post.total_ratings = ratings.count()
        post.average_rating = ratings.aggregate(models.Avg('rating'))['rating__avg'] or 0
        post.save()

        return Response({'detail': 'Rating saved successfully.'})


class PostViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet
                  ):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        user = request.user
        posts = Post.objects.all()
        serialized_posts = []

        for post in posts:
            user_rating = None
            user_rating_obj = UserRating.objects.filter(post=post, user=user).first()
            if user_rating_obj:
                user_rating = user_rating_obj.rating

            serialized_post = self.serializer_class(post).data
            serialized_post['user_rating'] = user_rating
            serialized_posts.append(serialized_post)

        return Response(serialized_posts)
