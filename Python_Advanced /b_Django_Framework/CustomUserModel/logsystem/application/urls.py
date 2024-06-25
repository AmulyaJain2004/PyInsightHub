from django.urls import path
from application import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup_view),
    path('signin/', views.signin_view),
    path('forgotpwd/', views.forgot_password_view),
]
