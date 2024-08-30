from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = SimpleRouter()
router.register(r'courses', views.CoursesCRD)

lesson_router = DefaultRouter()
lesson_router.register(r'lessons', views.LessonsCRUD, basename='lessons')

commentcud = SimpleRouter()
commentcud.register(r'comments', views.CommentsCUD, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/lessons/', include(lesson_router.urls)),
    path('api/v1/<int:pk>/lessonsofcourse/', views.LessonsByCourses.as_view()),
    path('api/v1/purchase/<int:pk>/', views.Purchase.as_view()),
    path('api/v1/comments_by_lesson/<int:pk>/', views.CommentView.as_view()),
    path('api/v1/comments/', include(commentcud.urls))
]