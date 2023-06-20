"""
    Module is tasked with handling the business
    logic for all the views that come to this site
    MY VIEW IS VERY NOISE WITH UNWANTED
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
    SD_SHOP = 'A very simple shopin template for ' +\
    'show casing a description to be in the name of laughter'
    LD_SHOP = 'A very simple shopin template for ' 
    'show casing a long description of a shop description'
    list_of_shops = [{
        'Title': 'Shopin 1',
        'Description': SD_SHOP + 'This is specific to ',
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'red',
        'Moto':'Peace and Love'
    },{
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto':'Love over hate'
    },{
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto':'The Future is yours'
    },{
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto':'Be The Change'
    },{
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto':'Shop Right'
    },{
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto':'Shoping Made Easy'
    },{
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto':'Making the sales'
    }]
    shop = list_of_shops[0]
    shop['Description'] += shop['Title']
    # i want to display a list of hostels which are top rated
    for shop in list_of_shops:
        # create a new item in a shop
        rating = shop['Rating'].split(' ')
        if int(rating[0]) != 5:
            shop['is_top_rated'] = False
        else:
            shop['is_top_rated'] = True
    
    # in other to ensure separation of concerns
    # i will be getting each individual peace of data
    top_rated = [shop for shop in list_of_shops if shop['is_top_rated']][:3]
    context = {'shop_list':list_of_shops,
               'top_rated':top_rated,
               'length':
               [len(shop['Description']) for shop in list_of_shops]} #context to display to the home page
    return render(request, 'shopin/index.html', context=context)