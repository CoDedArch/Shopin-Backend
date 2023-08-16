# Generated by Django 4.1.3 on 2023-08-16 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_product_coupon_rate_alter_product_discount_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='weekend bonanza', max_length=30, verbose_name='title on coupon')),
                ('coupon_rate', models.PositiveSmallIntegerField(default=0)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='coupon_rate',
        ),
        migrations.AddField(
            model_name='product',
            name='coupon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.coupon'),
        ),
    ]
