from django.db import models
from shopin.models import Shop

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="product name")
    shortdescription = models.TextField(max_length=300, verbose_name="product short description")
    longdescription = models.TextField(max_length=300, verbose_name="product long description")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, verbose_name='product status', blank=True)
    quantity = models.IntegerField(default=1, verbose_name='product quantity')
    warrantyears = models.IntegerField(blank=True, default= 0)
    created_date = models.DateField(auto_now_add=True)

    # has a relationship with product
    shop = models.ForeignKey(Shop, related_name='shop_products', on_delete=models.CASCADE) 
    shopingCart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return (f'product - {self.name}')
    

    def save(self, *args, **kwargs):
        if self.quantity:
            self.status = 'in-stock'
        self.status = 'out-of-stock'
        super().save(*args, **kwargs)




class ShoppingCart(models.Model):
    datecreated = models.DateField(auto_now_add=True)
    customer = models.OneToOneField('customers.Customer', default=None, on_delete= models.CASCADE, null=True)

    def __str__(self) -> str: 
        return (f"{self.customer.first_name} - shopping Cart")
    
    # i going to prevent the user from saving a cart which already exists
    @classmethod
    def prevent_double_carts(cls, cart_name):
        if cart_name in cls.objects.all():
            raise ValueError(f'{cart_name} already exists')
        return False
        
    def save(self, *args, **kwargs):
        cart_save_name = f'{self.customer.first_name} - shopping Cart'
        if not ShoppingCart.prevent_double_carts(cart_name=cart_save_name):
            super().save(*args, **kwargs)

    
class Order(models.Model):
    customer = models.ForeignKey('customers.Customer',default=None, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return (f'{self.customer.first_name} - Order')

