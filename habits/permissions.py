from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только владельцу привычки.
    """
    def has_object_permission(self, request, view, obj):
        # Если это безопасный метод (GET, HEAD, OPTIONS) и привычка публичная
        if request.method in permissions.SAFE_METHODS and obj.is_public:
            return True
        # В остальных случаях проверяем владельца
        return obj.user == request.user