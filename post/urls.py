from rest_framework import routers
from django.urls import path, include

from post.views import PostViewSet, FollowAPIView, UnfollowAPIView


router = routers.DefaultRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls), name='posts'),
    path('<int:uid>/', include(router.urls), name='posts'),
    path('<int:uid>/follow/', FollowAPIView.as_view(), name='follow'),
    path('<int:uid>/unfollow/', UnfollowAPIView.as_view(), name='unfollow'),
]
