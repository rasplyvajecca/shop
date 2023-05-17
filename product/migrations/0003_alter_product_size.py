# Generated by Django 4.2 on 2023-05-17 20:03

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_categories_category_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'M'), ('S', 'S'), ('XL', 'XL'), ('L', 'L')], max_length=50, verbose_name='Размер'),
        ),
    ]
