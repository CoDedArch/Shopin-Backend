"""
    contains my data layer to access
    sqlite database
"""
from django.db import models
from pathlib import Path
import csv


class Shop(models.Model):
    """
        A Table representing a Shop object
        contains functionalities of a Shop
    """
    PATH_TO_CSV = Path(__file__).resolve().parent.parent
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


# instantiating
# Shop.instantiate_SHP_from_csv()
