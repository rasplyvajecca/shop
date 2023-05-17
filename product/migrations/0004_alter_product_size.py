# Generated by Django 4.2 on 2023-05-17 20:15

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XL', 'XL'), ('L', 'L'), ('S', 'S'), ('M', 'M')], max_length=50, verbose_name='Размер'),
        ),
    ]
