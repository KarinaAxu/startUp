from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("store.can_view_dish") or request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user or request.user.is_staff
