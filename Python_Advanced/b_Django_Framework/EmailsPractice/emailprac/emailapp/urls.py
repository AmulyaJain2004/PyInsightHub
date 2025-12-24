from django.urls import path
from emailapp import views

urlpatterns = [
    path('send-email/', views.send_test_email, name='send_email'),
    path('register/', views.register, name='register'),
]
