from django.db import models
from shopin.models import Shop
from customers.models import Customer

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
    shopingCart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return (f'product - {self.name}')



class ShoppingCart(models.Model):
    datecreated = models.DateField(auto_now_add=True)
    customer = models.OneToOneField(Customer, on_delete= models.CASCADE)

    def __str__(self) -> str: 
        return (f"{self.customer.first_name} - shopping Cart")
    
class Orders(models.Model):
    customer = models.ManyToManyField(Customer, on_delete=models.CASCADE)

