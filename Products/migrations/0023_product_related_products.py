# Generated by Django 4.1.3 on 2023-08-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0022_aboutproduct_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, to='Products.product'),
        ),
    ]