from django.db import models
from multiselectfield import MultiSelectField


class Categories(models.Model):
    name = models.CharField(max_length=50)
    CHOICE_GROUP = {
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children')
    }
    category = models.CharField('Категория', max_length=50, choices=CHOICE_GROUP)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Shop(models.Model):
    name = models.CharField('Название', max_length=50)
    about = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=0)
    img = models.ImageField('Фото', upload_to='main/static/main/img/', blank=True)
    availability = models.BooleanField('Наличие')
    SIZE_CHOICES = {
                    ('S', 'S'),
                    ('M', 'M'),
                    ('L', 'L'),
                    ('XL', 'XL')}
    size = MultiSelectField('Размер', choices=SIZE_CHOICES, max_choices=4, max_length=50)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
