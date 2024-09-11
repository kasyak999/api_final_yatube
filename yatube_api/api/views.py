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
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,]
    pagination_class = None

    def getting_post(self):
        return Post.objects.get(pk=self.kwargs['post_pk'])

    def get_queryset(self):
        return self.getting_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.getting_post()
        )


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """получаем информацию о группе."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class FollowViewSet(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
