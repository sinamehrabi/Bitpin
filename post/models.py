from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class UserRating(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

    class Meta:
        unique_together = ('user', 'post')
