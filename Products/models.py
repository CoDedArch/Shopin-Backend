from django.db import models
from shopin.models import Shop
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="product name")
    shortdescription = models.TextField(max_length=300, verbose_name="product short description")
    longdescription = models.TextField(max_length=300, verbose_name="product long description")
    cost = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=100, verbose_name='product status')
    quantity = models.IntegerField(default=1, verbose_name='product quantity')
    warrantyears = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    
    # has a relationship with product
    shop = models.ForeignKey(Shop, related_name='shop_products', on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return (f'product - {self.name}')
    