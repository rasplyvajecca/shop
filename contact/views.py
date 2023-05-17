from django.shortcuts import render
from django.shortcuts import redirect
from .models import Feedback


def create(request):
    feedback = Feedback()
    feedback.name = request.POST.get("name")
    feedback.surname = request.POST.get("surname")
    feedback.email = request.POST.get("email")
    feedback.about = request.POST.get("about")
    feedback.message = request.POST.get("message")
    feedback.save()

    return redirect('/')


def contact(request):
    return render(request, 'contact/contact.html')


