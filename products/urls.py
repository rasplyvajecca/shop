from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="catalog"),
    path('<str:id>', views.detail, name="product"),
    ]