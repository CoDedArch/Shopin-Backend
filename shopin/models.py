"""This module contains models for shopin """
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)
from django.contrib.auth.models import User

from django.db import models 
from django.core.validators import MaxLengthValidator, MinLengthValidator

#do some logging
print(dir(BaseUserManager))

#create a custom user manager to handle some business logic of creating a user and a super user 
class CustomUserManager(BaseUserManager):
    def create_user(self, email: models.EmailField, password: str = None,
                    **extra_fields : dict) -> User:
        """This method returns a user"""

        if not email:
            raise ValueError('The email field is required')
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email:models.EmailField, password:str = None,
                        **extra_fields:dict) -> User:
        """This method is going to return a super user """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class customUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length= 20)
    zip = models.CharField(max_length=12)
    emailVerified = models.BooleanField(default= 0)
    registrationDate = models.DateTimeField(auto_now_add = True)
    verificationCode = models.CharField(max_length=20)
    ip = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=50 , null=True)
    # assign the query manager to the objects 
    objects = CustomUserManager()
    
    




class Products(models.Model):
    #relations 
    productCategory = models.ForeignKey('productCategories', on_delete=models.CASCADE, blank=False)
    productSKU = models.CharField(verbose_name='Product SKU',max_length=50,validators=[MaxLengthValidator(50)], unique=True)
    productName = models.CharField(verbose_name = 'Product Name',max_length=100)
    productPrice = models.DecimalField(verbose_name='Product Price',max_digits=10, decimal_places=2)
    productWeight = models.DecimalField(verbose_name='name of product', max_digits= 10, decimal_places= 2, null= True)
    productCartDesc = models.CharField(verbose_name='Product Cart Desc', max_length=255)
    productShortDesc = models.CharField(verbose_name='Product Short Desc',max_length=1000)
    productLongDesc = models.TextField()
    productThumb = models.CharField(verbose_name='Product Thumb',max_length=100)
    productImage = models.CharField(verbose_name = 'product image', max_length=100)
    productUpdateDate = models.DateTimeField(auto_now= True)
    productCreationDate = models.DateTimeField(auto_now_add= True)
    productStock = models.DecimalField(verbose_name='Product Stock', max_digits=10, decimal_places=2)
    # I will have to return and research into the product live 
    productLive = models.BooleanField(verbose_name='Product Live')
    productUnlimited = models.BooleanField(verbose_name='product Unlimited')
    productLocation = models.CharField(max_length=250, null=True)
    

    #methods to maintain state of the boject
    def __str__(self):
        return (f'{self.productName} -- {self.productPrice}')







#groups that products can belong to
class OptionGroups(models.Model):
    optionGroupName = models.CharField(verbose_name='Option Group Name', max_length= 50)

class Options(models.Model):
    optionName = models.CharField(verbose_name='option Name', max_length=50)
    optionGroups = models.ForeignKey(OptionGroups,on_delete= models.CASCADE)
    #there exist a many to many relationship between options and products through the junction table 
    product = models.ManyToManyField(Products)



# product categorie table 
class ProductCategories(models.Model):
    categoryName = models.CharField(verbose_name ='Category Name' ,max_length=50, validators= [MinLengthValidator(2)])


# Order related models 
class OrderDetails(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)
    detailName = models.CharField(verbose_name = 'detail name',max_length=250)
    detailPrice = models.DecimalField(verbose_name='detail price',max_digits=10, decimal_places=2)
    detailSKU = models.CharField(verbose_name='detail stock keeping unit', max_length = 50)
    detailQuantity = models.IntegerField()


class Orders(models.Model):
    user = models.ForeignKey('Users', on_delete = models.CASCADE)
    orderAmount = models.DecimalField(verbose_name = 'order amount', max_digits= 10, decimal_places=2)
    orderShipName = models.CharField(verbose_name='ship Name',max_length=100)
    orderShipAddress = models.CharField(verbose_name='order ship address', max_length = 100)
    orderShipAddress2 = models.CharField(verbose_name='order ship address 2', max_length=100, null=True)
    orderCity = models.CharField(verbose_name='order city', max_length= 50)
    orderState = models.CharField(verbose_name='order state', max_length=50)
    orderZip = models.CharField(verbose_name='order zip' , max_length=20)
    orderCountry = models.CharField(verbose_name='order Country', max_length=50)
    orderPhone = models.CharField(verbose_name='order phone', max_length=20)
    # orderFax = models.CharField(verbose_name='order Fax', max_length=20)
    orderShipping = models.DecimalField(verbose_name='shipping address', max_digits=10, decimal_places=2, null=True)
    orderTax = models.DecimalField(verbose_name='order tax', max_digits=10, decimal_places=2, null=True)
    orderEmail = models.CharField(verbose_name='order email', max_length= 100)
    orderDate = models.DateTimeField(auto_now_add = True)
    orderShipped = models.BooleanField(verbose_name='order shipped')
    orderTrackingNumber = models.CharField(verbose_name='order tracking number', max_length = 80, null=True)

#we want to create a custom user for our project 





