# Generated by Django 4.1.3 on 2023-08-18 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_alter_product_brand_alter_product_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='description title')),
                ('body', models.TextField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='longdescription',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.description'),
        ),
    ]
