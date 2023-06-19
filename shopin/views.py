"""
    Module is tasked with handling the business
    logic for all the views that come to this site
"""
from django.conf import settings
from django.shortcuts import render
import os

# Create your views here.
def home_page(request):
    """
        Returns the home page for Shopin
        Since this i will be loading a template
        i will not be using an HttpResponse 
        but a render 
    """
    SD_SHOP = 'A very simple shopin template for show casing a description'
    LD_SHOP = 'A very simple shopin template for show casing a description'
    list_of_shops = [{
        'Title': 'Shopin 1',
        'Description': SD_SHOP,
        'location': 'Tumu',
        'rating': '5 stars'
    },{
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'location': 'Tumu',
        'rating': '5 stars'
    },{
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'location': 'Tumu',
        'rating': '5 stars'
    },{
        'Title': 'Shopin 4',
        'Description': SD_SHOP,
        'location': 'Tumu',
        'rating': '5 stars'
    }]
    context = {'shop_list':list_of_shops} #context to display to the home page
    return render(request, 'shopin/index.html', context=context)