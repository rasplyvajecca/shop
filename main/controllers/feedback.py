from django.shortcuts import redirect
from contact.models import Feedback


def create(request):
    feedback = Feedback()
    feedback.name = request.POST.get("name")
    feedback.surname = request.POST.get("surname")
    feedback.email = request.POST.get("email")
    feedback.about = request.POST.get("about")
    feedback.message = request.POST.get("message")
    feedback.save()

    return redirect('/')