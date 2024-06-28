from django.urls import path, include
from drf_api2 import views

urlpatterns = [
    path('', views.home),
    path('student/', views.post_student)
]
