from rest_framework import permissions


class IsOwnerOrReadOnlyCallAndEvent(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.organisation.user == request.user or request.user.is_staff


class IsOwnerOrReadOnlyOrgAndVol(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff


class IsOwnerOrReadOnlyCallOption(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.call.organisation.user == request.user or request.user.is_staff
