# Generated by Django 4.1.3 on 2023-08-08 21:45

import Products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=Products.models.upload_product_image),
        ),
    ]