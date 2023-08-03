from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class ViewProducts(View):
    def get(self, request, shop_name):
        # get all products related to a particular shop
        all_products = Product.objects.filter(shop = shop_name)
        print(all_products)
        return render(request, template_name='products/products.html')
