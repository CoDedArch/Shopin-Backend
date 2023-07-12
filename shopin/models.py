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
    Title = models.CharField(max_length=100, default='',
                             verbose_name='SHP_Name')
    Description = models.TextField(default='',
                                   verbose_name='SHP_Description',
                                   max_length=270)
    Location = models.CharField(max_length=30, default='',
                                verbose_name='SHP_Location')
    Rating = models.IntegerField(default=0,
                                 verbose_name='SHP_Rating')
    Color = models.CharField(max_length=20, default='black')
    Moto = models.CharField(max_length=100,
                            verbose_name='SHP_Moto')

    def __str__(self):
        # return the string representation for each repr
        return self.Title + '--' + self.Location
    
    __repr__ = __str__

    @classmethod
    def instantiate_SHP_from_csv(cls):
        """This method will read from an CSV file and instantiate the obj"""
        with open('%s/modules/ShopTest.csv' % (Shop.PATH_TO_CSV), 'r') as SHP_info:
            reader = csv.DictReader(SHP_info)
            list_of_shop = list(reader)
        for shop in list_of_shop:
            Shop.objects.create(
                Title=shop['Title'],
                Description=shop['Description'],
                Location=shop['Location'],
                Rating=int(shop['Rating']),
                Color=shop['Color'],
                Moto=shop['Moto']
            )
    # create an instance method 
    def check_is_top_rated(self):
        """checks whether an instance is top rated"""
        if self.Rating == 5:
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
        for count in range(3):
            random_index = random.randint(0,2)
            three_random_top_rated_shop.append(cls.all_top_rated()[random_index])

        return three_random_top_rated_shop



def upload_image_to(instance, filename):
    return 'images/%s/%s'%(instance.id, filename)
    

# instantiating
# Shop.instantiate_SHP_from_csv()
class Category(models.Model):
    """This repr a category and some functionality that it can contain"""
    name = models.CharField(max_length=60,
                        verbose_name='Category')
    # read more into working with image field
    image = models.ImageField(upload_to=upload_image_to)
    has_subsection = models.BooleanField(default=False)
    section = models.OneToOneField('Section',on_delete=models.CASCADE)
    # create a custom logic
    @classmethod
    def assign_to_nothing(cls):
        if cls.section.contains_products_only:
            # retrieve all products from products table
            # assign to section
            cls.section['products'] = []
            

# have the many relationship
class Section(models.Model):
    name = models.CharField(max_length=60,
                            verbose_name='section_name') 
    contains_products_only = models.BooleanField(default=False)
    color = models.CharField(max_length=20)
    pagnation_unit = models.SmallIntegerField()
