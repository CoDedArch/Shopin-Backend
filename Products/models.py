from django.db import models
from shopin.models import Shop
import decimal

# Create your models here.
def upload_product_image(instance, filename):
    """Returns the path to upload the product image to"""
    
    return f"images/products/{instance.name}/{filename}"


class Brand(models.Model):
    brand = models.CharField(max_length=100, verbose_name='brand_name')

    def __str__(self) -> str:
        return ('Brand: %s'%(self.brand))


class Description(models.Model):
    title = models.CharField(max_length=40, verbose_name='description title' )
    body = models.TextField(max_length=250)

class Product(models.Model):
    """Model for a Product object"""

    name = models.CharField(max_length=100, verbose_name="product name")
    shortdescription = models.TextField(max_length=300,
                                        verbose_name="product short " +
                                        "description")
    # longdescription = models.TextField(max_length=3000,
    #                                    verbose_name="product long description")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100,
                              verbose_name='product status',
                              blank=True)
    quantity = models.IntegerField(default=1,
                                   verbose_name='product quantity')
    warrantyears = models.IntegerField(blank=True, default=0)
    created_date = models.DateField(auto_now_add=True)
    issponsored = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_product_image)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, default= 0.00, verbose_name='amount payable after discount')
    discount_rate = models.PositiveSmallIntegerField(null=True, default=0)
    # if a customer has a coupon, he or she can purchase the product at the discount rate
    # has a relationship with product
    shop = models.ForeignKey(Shop, related_name='shop_products',
                             on_delete=models.CASCADE)
    shopingCart = models.ForeignKey('ShoppingCart',
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              null=True, blank=True)
    section = models.ForeignKey('shopin.Section',
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    category = models.ForeignKey("shopin.Category",
                                 on_delete=models.CASCADE,
                                 null=True, blank=True)
    subcategory = models.ForeignKey('shopin.Subcategory',
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    # products will relate to a coupon
    coupon = models.OneToOneField('Coupon', on_delete=models.CASCADE, null= True, blank=True)

    description = models.ForeignKey(Description, on_delete= models.CASCADE, null= True)

    def __str__(self) -> str:
        return (f'product - {self.name}-{self.shop.title}')

    @property
    def compute_discounted_cost(self):
        """Returns the cost of a product after computing the rate of discount on the original cost"""
        convert_rate = decimal.Decimal(self.discount_rate / 100)
        print(convert_rate, end= ' ')
        print(self.cost)
        discount_amount = convert_rate * self.cost
        print(discount_amount)
        amount_payable = round((self.cost - discount_amount), 2)
        print(amount_payable)
        return amount_payable
    
    @property
    def sectionBelongsToShop(self) -> True or ValueError:
        """Checks if a section is associated with this shop"""

        if self.shop.title == self.section.shop.title:
            return True
        else:
            raise ValueError('Section and Shop selected are not related')

    @property
    def sectionAcceptsProductOnly(self) -> bool:
        """Checks if a section accepts only products"""

        return (self.section.contains_products_only)

    @property
    def categoryBelongsToShop(self) -> True or ValueError:
        """Checks if a category a product belongs to
        is associated with this Shop"""

        if self.category.shop.title == self.shop.title:
            return True
        else:
            raise ValueError('category and shop are not related')

    @property
    def subcategoryBelongsToShop(self):
        """Checks if the subcategory selected
        is associated with a shop"""

        if self.subcategory.category.shop.title == self.shop.title:
            return True
        else:
            raise ValueError('SubCategory and Shop selected are not related')

    def save(self, *args, **kwargs):
        """Overrides the save method and saves a product"""

        self.status = 'in-stock'
        if self.quantity == 0:
            self.status = 'out-of-stock'

        if self.discount_amount == 0.00 and self.discount_rate >= 0:
            self.discount_amount = self.compute_discounted_cost

        # before i save i need to know whether
        # or not the section accepts only
        # products and whether or not the section
        # belongs to the given shop
        if self.section:
            if self.sectionBelongsToShop and self.sectionAcceptsProductOnly:
                super().save(*args, **kwargs)
            else:
                raise ValueError('Section does not accept only products')
        if self.category:
            if self.categoryBelongsToShop:
                super().save(*args, **kwargs)

        if self.subcategory:
            if self.subcategoryBelongsToShop:
                super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class ShoppingCart(models.Model):
    """Models the pushing cart in a real shop"""

    datecreated = models.DateField(auto_now_add=True)
    customer = models.OneToOneField('customers.Customer',
                                    default=None,
                                    on_delete=models.CASCADE,
                                    null=True)

    def __str__(self) -> str:
        return (f"{self.customer.first_name} - shopping Cart")

    # i going to prevent the user from saving a cart which already exists
    @classmethod
    def prevent_double_carts(cls, cart_name):
        """Make sure that we don't have a repeated cart for a user"""

        if cart_name in cls.objects.all():
            raise ValueError(f'{cart_name} already exists')
        return False

    def save(self, *args, **kwargs):
        """Override the save method"""

        cart_save_name = f'{self.customer.first_name} - shopping Cart'
        if not ShoppingCart.prevent_double_carts(cart_name=cart_save_name):
            super().save(*args, **kwargs)


class Order(models.Model):
    """Models an Order Made on Products in an Ecommerce website"""

    customer = models.ForeignKey('customers.Customer',
                                 default=None,
                                 on_delete=models.CASCADE,
                                 null=True)

    def __str__(self) -> str:
        return (f'{self.customer.first_name} - Order')
    

class Coupon(models.Model):
    title = models.CharField(max_length=30, default='weekend bonanza', verbose_name='title on coupon')
    coupon_rate = models.PositiveSmallIntegerField(default=0)
    expiry_date = models.DateField()

    def __str__(self) -> str:
        return (f'coupon({self.title})-{self.coupon_rate}')
    