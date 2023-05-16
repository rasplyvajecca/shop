from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('', views.registration, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name="logout"),
    ]