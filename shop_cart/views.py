from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from order.models import Order, Item
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("catalog")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart(request):
    return render(request, 'shop_cart/cart_detail.html')


def checkout(request):
    return render(request, 'shop_cart/checkout.html')


def place_order(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        cart = request.session.get('cart')
        order = Order(
            user = user
        )
        order.save()
        for i in cart:
            a = (float(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            item = Item(
                order = order,
                product = cart[i]['name'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total
            )
            item.save()
    return render(request, 'shop_cart/thankyou.html')