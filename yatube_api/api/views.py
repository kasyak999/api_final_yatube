# TODO:  Напишите свой вариант
from posts.models import Post, Group, Follow
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer)
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework import filters
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import mixins


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """получаем список всех постов или создаём новый пост."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """получаем список комментариев."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    @property
    def getting_post(self):
        return get_object_or_404(
            Post, pk=self.kwargs['post_pk'])

    def get_queryset(self):
        return self.getting_post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.getting_post
        )


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """получаем информацию о группе."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#  class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin):
# class FollowViewSet(generics.ListCreateAPIView):
class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
