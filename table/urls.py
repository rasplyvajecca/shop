from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_home, name="table_home"),
    path('about/', views.about, name="about"),
]
