# Generated by Django 4.2 on 2023-05-17 20:38

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_categories_category_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'S'), ('XL', 'XL'), ('M', 'M'), ('L', 'L')], max_length=50, verbose_name='Размер'),
        ),
    ]