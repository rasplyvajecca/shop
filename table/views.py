from django.shortcuts import render
from .models import Shop


def table_home(request):
    table = Shop.objects.order_by('price')
    return render(request, 'table/table_home.html', {'table': table})


def about(request):
    return render(request, 'table/about.html')