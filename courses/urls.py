from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = SimpleRouter()
router.register(r'courses', views.CoursesCRD)

lesson_router = DefaultRouter()
lesson_router.register(r'lessons', views.LessonsCRUD, basename='lessons')

commentcud = SimpleRouter()
commentcud.register(r'comments', views.CommentsCUD, basename='comments')


socre_router = SimpleRouter()
socre_router.register(r'score', views.ScoreForCourses, basename='score')


urlpatterns = [
    path('api/v1/', include(lesson_router.urls)),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(commentcud.urls)),
    path('api/v1/', include(socre_router.urls)),
    path('api/v1/lessonsofcourse/<int:pk>/', views.LessonsByCourses.as_view()),
    path('api/v1/purchase/<int:pk>/', views.Purchase.as_view()),
    path('api/v1/comments_by_lesson/<int:pk>/', views.CommentView.as_view()),
]