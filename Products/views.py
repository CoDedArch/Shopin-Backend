from django.shortcuts import render
from django.views import View
from .models import Product
from shopin.models import Shop
# Create your views here.

class ViewProducts(View):
    def get(self, request, shop_name):
        # get all products related to a particular shop
        try:
            requested_shop = Shop.objects.get(title=shop_name)
        except Shop.DoesNotExist:
            pass

        all_products = Product.objects.filter(shop = requested_shop)
        print(all_products)
        return render(request, template_name='products/products.html')
