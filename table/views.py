from django.shortcuts import render
from .models import Shop


def table_home(request):
    table = Shop.objects.order_by('price')
    return render(request, 'table/shop.html', {'table': table})


