from django.db import models

from bitpin.base_model import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    total_ratings = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)


class UserRating(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

    class Meta:
        unique_together = ('user', 'post')
