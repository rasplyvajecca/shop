from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('', include('main.urls')),
    path('shop/', include('contact.urls')),
    path('registration/', include('users.urls')),
    path('cart/', include('shop_cart.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
