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


class LessonsPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if (obj.courses.subscribers.filter(id = user.id).exists() and request.method == 'GET') or request.user.is_staff:
            return True
        elif request.user == obj.courses.creator or request.user.is_staff == True:
            return True
        else:
            return False