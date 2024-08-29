from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .permissions import CoursesCRDpermissions, LessonsPermission
from .serializers import CourseSerializer, LessonsSerializer, LessonsSerializerShort
from .models import Course, Lessons


class CoursesCRD(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (CoursesCRDpermissions, )

    #переписать retreive (чтобы возвращал все уроки связаные с курсом (коротко))

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return Course.objects.filter(Q(course_title__contains = search) | Q(lesson_intro__contains = search))
        else:
            return Course.objects.all()


class Purchase(APIView):
    permission_classes = (IsAuthenticated, )
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            course = Course.objects.get(pk = self.kwargs.get('pk'))
        except:
            return Response({'error': 'course does not exist', 'pk': self.kwargs.get('pk')})
        
        if course.subscribers.filter(id=user.id).exists():
            return Response({'error': 'the course has already been purchased'})

        if user.balance.balance >= course.price:
            try:
                user.balance.balance -= course.price
                course.subscribers.add(user)
                course.save()
                user.balance.save()
                return Response({'purchase': 'course has been successfully purchased', 'balance': user.balance.balance})
            except:
                return Response({'error': 'somehing went wrong'})
        else:
            return Response({'error': 'course is too expensive'})
        

class LessonsCRUD(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (LessonsPermission, )

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        obj = self.get_object()

        if not obj.viewed_by.filter(id=user.id).exists():
            obj.viewed_by.add(user)
        
        serialized = self.get_serializer(obj)
        return Response(serialized.data)
    
    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET' and not self.request.kwargs.get('pk'):
            return LessonsSerializerShort(*args, **kwargs)
        else: 
            return LessonsSerializer(*args, **kwargs)