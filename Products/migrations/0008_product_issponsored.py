# Generated by Django 4.1.3 on 2023-08-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='issponsored',
            field=models.BooleanField(default=False),
        ),
    ]
