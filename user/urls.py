from django.urls import path, include, re_path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('api/v1/profile/<slug:slug>/', views.Profile.as_view()),
    path('api/v1/register/', views.Register.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]
