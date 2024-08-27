from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.user == obj and request.method in ['PUT', 'PATCH']:
            return True
        
        elif request.method == 'GET':
            return True
        
        else:
            return False
    
