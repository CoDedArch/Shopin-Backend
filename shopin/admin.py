"""This module helps me register to the admin interface"""
from django.contrib import admin
from . import models as shopin_models 

# we can also have the admin for each model on the site 

class ShopAdmin(admin.ModelAdmin):
    pass

class SectionAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class SubCategoryAdmin(admin.ModelAdmin):
    pass

# register a model
admin.site.register(shopin_models.Shop)
admin.site.register(shopin_models.Section)
admin.site.register(shopin_models.Category)
admin.site.register(shopin_models.SubCategory)
