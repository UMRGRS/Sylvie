from rest_framework import permissions

# Permission to only allow company admins to modify machines data
class IsCompanyAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_company_admin