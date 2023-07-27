from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
# Create your models here.
# customer will have to inherit from user model
class Customer(User, models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)


class Reviews(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reviewContent = models.TextField(verbose_name='content for review')
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
