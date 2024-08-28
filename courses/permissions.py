from rest_framework import permissions    


class CoursesCRDpermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        else:
            return True


    def has_object_permission(self, request, view, obj):
        if (request.user == obj.creator and request.method in ['PUT', 'PATCH', 'DELETE']) or request.user.is_staff == True:
            return True
        
        elif request.method == 'GET':
            return True

        else:
            return False
