from django.shortcuts import render
from .models import Shop, Categories


def shop(request):
    products = Shop.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    PRICE_LOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID = request.GET.get('PRICE_HIGHTOLOW')
    if CATID:
        products = Shop.objects.filter(categories=CATID)
    elif PRICE_LOWTOHIGHID:
        products = Shop.objects.order_by('price')
    elif PRICE_HIGHTOLOWID:
        products = Shop.objects.order_by('-price')
    context = {'products': products,
               'categories': categories}
    return render(request, 'products/shop.html', context)


def detail(request,id):
    el = Shop.objects.filter(id=id).first()
    return render(request, 'products/shop-single.html', {'el': el})
