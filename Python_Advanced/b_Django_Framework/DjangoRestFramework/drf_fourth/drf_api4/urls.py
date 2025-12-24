from django.urls import path, include
from drf_api4 import views

urlpatterns = [
    path('', views.home),
    path('student/', views.post_student),
    path('update-student/<id>/', views.update_student),
    path('update-student-patch/<id>/', views.update_student_patch),
]
