from django.urls import path, re_path

from . import views

urlpatterns = [
    path('getuser/', views.getUser, name='getuser'),
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signupUser, name='signup'),
]