from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# customer will have to inherit from user model
class Customer(User, models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    


class Reviews(models.Model):
    reviewContent = models.TextField(verbose_name='content for review')
    rating = models.IntegerField()
    product = models.ForeignKey('Products.Product', on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer,default=None, on_delete=models.CASCADE)

