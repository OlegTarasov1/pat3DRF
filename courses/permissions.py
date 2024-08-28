from rest_framework import permissions    


class CoursesCRDpermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        elif request.method == 'POST' and request.user.is_authenticated :
            return True 

        else:
            return False         


    def has_object_permission(self, request, view, obj):
        if (request.user == obj.creator and request.method in ['PUT', 'PATCH']) or request.method == 'GET':
            return True
        
        else:
            return False