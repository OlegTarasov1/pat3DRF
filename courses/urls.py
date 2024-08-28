from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'courses', views.CoursesCRD)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/purchase/<int:pk>/', views.Purchase.as_view())
]