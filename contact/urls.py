from django.urls import path
from . import views
from main.controllers import feedback

urlpatterns = [
    path('', views.contact, name="contact"),
    path('feedback/', feedback.create)
    ]