"""This module helps me register to the admin interface"""
from django.contrib import admin
from . import models as shopin_models 
# register a model
admin.site.register(shopin_models.Shop)
admin.site.register(shopin_models.Section)
admin.site.register(shopin_models.Category)
admin.site.register(shopin_models.SubCategory)
