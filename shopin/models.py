"""
    contains my data layer to access
    sqlite database
"""
from django.db import models
from pathlib import Path
import random
import csv


class Shop(models.Model):
    """
        A Table representing a Shop object
        contains functionalities of a Shop
    """
    PATH_TO_CSV = Path(__file__).resolve().parent.parent
    top_rated = []
    title = models.CharField(max_length=100, default='',
                             verbose_name='SHP_Name')
    description = models.TextField(default='',
                                   verbose_name='SHP_Description',
                                   max_length=270)
    location = models.CharField(max_length=30, default='',
                                verbose_name='SHP_Location')
    rating = models.IntegerField(default=0,
                                 verbose_name='SHP_Rating')
    color = models.CharField(max_length=20, default='black')
    moto = models.CharField(max_length=100,
                            verbose_name='SHP_Moto')

    def __str__(self):
        # return the string representation for each repr
        return self.title + '--' + self.location
    
    __repr__ = __str__

    @classmethod
    def instantiate_SHP_from_csv(cls):
        """This method will read from an CSV file and instantiate the obj"""
        with open('%s/modules/ShopTest.csv' % (Shop.PATH_TO_CSV), 'r') as SHP_info:
            reader = csv.DictReader(SHP_info)
            list_of_shop = list(reader)
        for shop in list_of_shop:
            Shop.objects.create(
                title=shop['Title'],
                description=shop['Description'],
                location=shop['Location'],
                rating=int(shop['Rating']),
                color=shop['Color'],
                moto=shop['Moto']
            )
    # create an instance method 
    def check_is_top_rated(self):
        """checks whether an instance is top rated"""
        if self.rating == 5:
            return True
        return False
    
    # randomly generate the three top rated shop
    @classmethod
    def all_top_rated(cls):
        """returns all top rated shop instances"""
        return [
            shop
            for shop in cls.objects.all()
            if shop.check_is_top_rated()
        ]
    @classmethod
    def randomly_fetch_three_top_rated(cls):
        """randomly pick three top rated
           from the all top rated shop
        """
        three_random_top_rated_shop = []
        # i will have to make sure that this refreshes after a day is over
        for count in range(3):
            random_index = random.randint(0,2)
            three_random_top_rated_shop.append(cls.all_top_rated()[random_index])

        return three_random_top_rated_shop


def upload_image_to(instance, filename):
    if instance.__class__.__name__ == 'Category':
        return 'images/category/%s/%s'%(instance.name, filename)
    elif instance.__class__.__name__ == 'SubCategory':
        return 'images/subcategory/%s/%s'%(instance.name, filename)
    
# have the many relationship
class Section(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,
                            verbose_name='section_name', blank=True, null=True)
    # contains_products_only = models.BooleanField(default=False)
    contains_category = models.BooleanField(default=False)
    color = models.CharField(max_length=20)
    pagnation_unit = models.SmallIntegerField()
    
    def __str__(self) -> str:
        if self.name:
            return f"section: {self.name} will contain only products: {self.contains_products_only}"
        return f"section of:{self.shop.title} will contain only products:{self.contains_products_only}"

    @property
    def contains_products_only(self):
        return not self.contains_category
    
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.contains_category = self.category.exists()

    

class Category(models.Model):
    """This repr a category and some functionality that it can contain"""
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,
                        verbose_name='Category')
    # read more into working with image field
    image = models.ImageField(upload_to=upload_image_to, null=True, blank= True)
    wants_subcategory = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'category-{self.name}'
    
    def save(self, *args, **kwargs):
        if self.section.shop.title == self.shop.title: 
            if self.section.contains_category:
                super().save(*args, **kwargs)
            else:
                raise ValueError('Section should accept category before it can be saved')
        else:
            raise ValueError('You must select a section inside a shop')

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_image_to)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.category.wants_subcategory:
            super(SubCategory, self).save(*args, **kwargs)
        else:
            raise ValueError("This cateogry does not support subcategories")