from rest_framework import permissions    


class CoursesCRDpermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        else:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.creator
        
        elif request.method == 'GET':
            return True

        else:
            return False
