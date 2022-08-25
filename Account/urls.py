from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('user/', views.signUp),
    path('user/<str:username>/', views.user_setting),
    path('email_pass/<str:username>/', views.email_verification),
    path('find_pw/', views.find_pw)
]