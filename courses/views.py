from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .permissions import CoursesCRDpermissions, LessonsPermission, ScorePermission, CommentsPermission
from .serializers import CourseSerializer,  ScoreSerializer, LessonsSerializer, LessonsSerializerShort, SerializeComment
from .models import Course, Lessons, Comments, Score


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
    permission_classes = (LessonsPermission, )

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        obj = self.get_object()

        if not obj.viewed_by.filter(id=user.id).exists():
            obj.viewed_by.add(user)
        
        serialized = self.get_serializer(obj)
        return Response(serialized.data)
    
    def get_serializer(self, *args, **kwargs):
        try:
            if self.request.method == 'GET' and not self.request.kwargs.get('pk'):
                return LessonsSerializerShort(*args, **kwargs)
        except:
            return LessonsSerializer(*args, **kwargs)
        

class LessonsByCourses(generics.ListAPIView):
    
    serializer_class = LessonsSerializerShort
    permission_classes = (LessonsPermission, )

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Lessons.objects.filter(courses__id = pk)


class CommentView(APIView):
    queryset = Comments.objects.all()
    serializer_class = SerializeComment
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comments = Comments.objects.filter(lesson_id = pk)
        out = []
        for i in comments:
            serialized = self.serializer_class(i)
            out.append(serialized.data)
        return Response(out)
    

class CommentsCUD(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = Comments.objects.all()
    serializer_class = SerializeComment
    permission_classes = (CommentsPermission, )


class ScoreForCourses(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = (ScorePermission, )
