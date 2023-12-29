from django.urls import path, include
from post.urls import rate_router, post_router

urlpatterns = [
    path('posts/', include(post_router.urls)),
    path('posts/<str:post_id>/rates/', include(rate_router.urls)),
]
