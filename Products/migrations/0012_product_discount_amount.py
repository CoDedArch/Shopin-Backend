# Generated by Django 4.1.3 on 2023-08-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_brand_alter_product_longdescription_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
    ]
