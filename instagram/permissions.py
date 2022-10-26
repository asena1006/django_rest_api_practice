from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    #인증이 되어야만 목록조회, 포스팅 등록 가능
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
