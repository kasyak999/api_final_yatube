from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """Проверяет, является ли пользователь автором объекта."""
    def has_object_permission(self, request, view, obj):
        print(SAFE_METHODS)
        return obj.author == request.user or request.method in SAFE_METHODS
