# Generated by Django 4.1.3 on 2023-09-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0024_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='what users should be concerned with'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty_and_support',
            field=models.TextField(blank=True, max_length=550, null=True),
        ),
    ]
