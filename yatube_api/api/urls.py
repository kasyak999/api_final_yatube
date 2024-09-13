from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupsViewSet, FollowViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post_all')
router.register(
    r'posts/(?P<post_pk>\d+)/comments', CommentViewSet,
    basename='post-comments')
router.register('groups', GroupsViewSet)
router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
