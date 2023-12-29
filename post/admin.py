from django.contrib import admin
from django.contrib.admin import ModelAdmin

from post.models import Post, UserRating


class PostAdmin(ModelAdmin):
    list_display = ('id', 'title', 'content', 'average_rating', 'total_ratings', 'created_at', 'updated_at')


class UserRateAdmin(ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at', 'updated_at')


admin.site.register(Post, PostAdmin)
admin.site.register(UserRating, UserRateAdmin)
