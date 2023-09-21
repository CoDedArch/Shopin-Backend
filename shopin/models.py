"""
    contains my data layer to access
    sqlite database
"""
from django.db import models
from pathlib import Path
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import random
import csv

def upload_image_to(instance, filename):
    saveLocations = {
        'category': 'images/category/%s/%s' % (instance.name, filename),
        'subcategory': 'images/subcategory/%s/%s' % (instance.name, filename),
        'shop': 'images/shop/%s/%s' % (instance.name, filename)
    }
    return (saveLocations.get(instance.__class__.__name__.lower(),
                              f'images/extra/{filename}'))



class Shop(models.Model):
    """
        A Table representing a Shop object
        contains functionalities of a Shop
    """
    PATH_TO_CSV = Path(__file__).resolve().parent.parent
    top_rated = []
    name = models.CharField(max_length=100, default='',
                             verbose_name='SHP_Name')
    email = models.EmailField(null=True)
    contactLine = models.CharField(max_length=20, null=True,
                                   verbose_name='contact')
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
    logo = ProcessedImageField(
        upload_to = upload_image_to,
        processors= [ResizeToFill(300, 300)],
        format= 'JPEG',
        options={'quality': 70},
        null = True
    )

    def __str__(self):
        # return the string representation for each repr
        return self.name + '--' + self.location

    __repr__ = __str__

    @classmethod
    def numberOfShops(cls):
        return (len(cls.objects.all()))
    
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
        no_top_rated = 3
        three_random_top_rated_shop = []
        # i will have to make sure that this refreshes after a day is over
        if cls.numberOfShops() < no_top_rated:
            three_random_top_rated_shop.extend(cls.objects.all())
        else:
            for count in range(no_top_rated):
                random_index = random.randint(0, 2)
                three_random_top_rated_shop.append(cls.all_top_rated()[random_index])

        return three_random_top_rated_shop
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
            return (f"section: {self.name} will contain " +
                    f"only products: {self.contains_products_only}")
        return (f"section of:{self.shop.title} will contain " +
                f"only products:{self.contains_products_only}")

    @property
    def contains_products_only(self) -> bool:
        """Checks if a section contains only products"""
        
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
    image = ProcessedImageField(upload_to = upload_image_to,
                                processors=[ResizeToFill(430,385)],
                                format='JPEG',
                                options={'quality':70}, null=True)
    wants_subcategory = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'category-{self.name}'

    @property
    def categoryContainsImage(self):
        if not self.wants_subcategory:
            return (True if self.image else False)
        return True

    def save(self, *args, **kwargs):
        if self.section:
            if self.section.shop.title == self.shop.title:
                if self.section.contains_category:
                    # i need to make sure that the category contains images
                    if not self.categoryContainsImage:
                        raise ValueError('Ensure that category contains an image')
                    super().save(*args, **kwargs)
                else:
                    raise ValueError('Section should accept category before it can be saved')
            else:
                raise ValueError('You must select a section inside a shop')
        else:
            super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = ProcessedImageField(upload_to=upload_image_to,
                                processors=[ResizeToFill(200,140)],
                                format='JPEG',
                                options={'quality':70})

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.category.wants_subcategory:
            super(SubCategory, self).save(*args, **kwargs)
        else:
            raise ValueError("This cateogry does not support subcategories")
