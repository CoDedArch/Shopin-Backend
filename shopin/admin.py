"""This module helps me register to the admin interface"""
from django.contrib import admin
from .models import Shop 
# register a model
admin.site.register(Shop)
