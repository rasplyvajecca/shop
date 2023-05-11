from django.db import models


class Shop(models.Model):
    title = models.CharField('Название', max_length=50)
    about = models.TextField('Описание', max_length=50)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=0)
    img = models.ImageField('Фото', upload_to='main/static/main/img/', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

