from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from .permissions import CoursesCRDpermissions
from .serializers import CourseSerializer
from .models import Course


class CoursesCRD(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (CoursesCRDpermissions, )

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return Course.objects.filter(Q(course_title__contains = search) | Q(lesson_intro__contains = search))
        else:
            return Course.objects.all()
        
    # def retrieve(self, request, *args, **kwargs):
    #     slug = request.kwargs.get('slug')
        
    #     try:
    #         course = self.get_queryset().get(course_slug = slug)
    #     except:
    #         return Response({'error': 'there was no object with such slug'})
    
    #     serializer = self.get_serializer(course)
    #     return Response(serializer.data)