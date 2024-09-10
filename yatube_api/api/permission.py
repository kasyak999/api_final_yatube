from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Проверяет, является ли пользователь автором объекта."""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method == 'GET'
