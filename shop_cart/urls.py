from django.urls import path
from . import views
from cart.cart import Cart

urlpatterns = [
    path('', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('thankyou/', views.place_order, name="thankyou"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart, name='cart_detail'),
    ]