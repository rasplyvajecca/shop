from django.shortcuts import render
from .models import Product, Categories


def shop(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    PRICE_LOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID = request.GET.get('PRICE_HIGHTOLOW')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    elif PRICE_LOWTOHIGHID:
        product = Product.objects.order_by('price')
    elif PRICE_HIGHTOLOWID:
        product = Product.objects.order_by('-price')
    context = {'product': product,
               'categories': categories}
    return render(request, 'product/shop.html', context)


def detail(request, id):
    prod = Product.objects.filter(id=id).first()
    return render(request, 'product/shop-single.html', {'prod': prod})
