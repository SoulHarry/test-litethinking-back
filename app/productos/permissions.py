from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Permiso personalizado para permitir a los administradores realizar cualquier acción,
    mientras que los usuarios no administradores solo pueden realizar operaciones de lectura.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS