# Generated by Django 4.1.3 on 2023-08-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0013_product_discount_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='coupon_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='amount payable after discount'),
        ),
    ]
