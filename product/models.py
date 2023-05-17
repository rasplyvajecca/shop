from django.db import models
from multiselectfield import MultiSelectField


class Categories(models.Model):
    name = models.CharField(max_length=255)
    CHOICE_GROUP = {
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children')
    }
    category = models.CharField('Категория', max_length=255, choices=CHOICE_GROUP)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    about = models.TextField('Описание')
    price = models.FloatField('Цена')
    image = models.ImageField('Фото', upload_to='products/')
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


