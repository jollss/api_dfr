    #permissions.py
from rest_framework import permissions
    
class IsOwner(permissions.BasePermission):
        message = "No es el propietario."
    
        def has_object_permission(self, request, view, obj):
                if request.method in permissions.SAFE_METHODS:
                        return True
                return request.user == obj.owners