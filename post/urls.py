from rest_framework import routers
from post.views import RatePostViewSet, PostViewSet

post_router = routers.SimpleRouter(trailing_slash=False)
post_router.register(r'', PostViewSet, basename='posts')

rate_router = routers.SimpleRouter(trailing_slash=False)
rate_router.register(r'', RatePostViewSet, basename='rates')
