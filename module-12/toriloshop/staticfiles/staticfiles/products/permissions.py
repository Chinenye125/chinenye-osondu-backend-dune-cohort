from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # SAFE METHODS (GET, HEAD, OPTIONS) allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # ONLY CREATOR CAN EDIT/DELETE
        return obj.created_by == request.user