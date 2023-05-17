# Generated by Django 4.2 on 2023-05-17 20:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_categories_category_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(choices=[('Children', 'Children'), ('Women', 'Women'), ('Men', 'Men')], max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('L', 'L'), ('XL', 'XL'), ('S', 'S'), ('M', 'M')], max_length=50, verbose_name='Размер'),
        ),
    ]
