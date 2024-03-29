# Generated by Django 4.2 on 2023-05-16 15:28

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Women', 'Women'), ('Men', 'Men'), ('Children', 'Children')], max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('about', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Фото')),
                ('size', multiselectfield.db.fields.MultiSelectField(choices=[('XL', 'XL'), ('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=50, verbose_name='Размер')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
