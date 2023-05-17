from django.db import models
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField('Название', max_length=255)
    quantity = models.CharField('Количество', max_length=255)
    price = models.FloatField('Цена')
    total = models.CharField('Итог', max_length=1000)