from django.shortcuts import render
from product.models import Product


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)
    context = {
        'product': product
    }
    return render(request, 'main/search.html', context)


