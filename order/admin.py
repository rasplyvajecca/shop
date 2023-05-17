from django.contrib import admin
from .models import *


class ItemTubleinline(admin.TabularInline):
    model = Item


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemTubleinline]


admin.site.register(Order)
admin.site.register(Item)