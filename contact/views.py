from django.shortcuts import render
from .models import Feedback


def table_home(request):
    return render(request, 'contact/contact.html')
