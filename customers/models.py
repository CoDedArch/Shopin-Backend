from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# customer will have to inherit from user model


class Customer(User, models.Model):
    """Customer inherits from the user model and models a customer object"""

    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    #  a customer can have many different coupons
    coupon = models.OneToOneField('Products.Coupon', on_delete=models.CASCADE, null=True, blank=True)



class Reviews(models.Model):
    """Reviews, a customer can review a product"""

    reviewContent = models.TextField(verbose_name='content for review')
    rating = models.IntegerField()
    product = models.ForeignKey('Products.Product',
                                on_delete=models.CASCADE,
                                null=True)
    customer = models.ForeignKey(Customer, default=None,
                                 on_delete=models.CASCADE)
