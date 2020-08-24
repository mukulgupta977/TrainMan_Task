from rest_framework.permissions import BasePermission


class IsCorrectUser(BasePermission):
    def has_permission(self, request, view):
        if request.data.get("user_id"):
            return request.user == request.data.get("user_id")
        return False
