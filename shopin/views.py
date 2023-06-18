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
    context = {} #context to display to the home page
    return render(request, 'shopin/index.html', context=context)