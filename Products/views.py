from django.shortcuts import render
from django.views import View
from .models import Product
from shopin.models import Shop, Category
# Create your views here.

class ViewCategoryProducts(View):
    def get(self, request, shop_name, category):
        # get all products related to a particular shop
        try:
            # do a test
            requested_category = Category.objects.get(name=category)
            if requested_category.shop.title == shop_name:
                products = requested_category.product_set.all()
        except Shop.DoesNotExist:
            pass
        
        for product in products:
            if product.discount_rate:
                print('hear')
        # Products = [{
        #     "image":'image1',
        #     'sponsored': True,
        #     'description': "GNMN Bluetooth Headphones Wireless Earbuds 48hrs Playback IPX7 Waterproof Ear Buds Over-Ear Stereo Bass Earphones with Earhooks Microphone LED Battery Display for Sports/Workout/Gym/Running Black",
        #     "rating":"5 stars",
        #     'discounted_amount': "$23.39",
        #     'price': '$27.99',
        #     'coupon': '20%',
        #     'Delivery': 'Delivery Thu, Aug 17',
        #     'destination': 'Ghana',
        #     'total_rating': '494'

        # },{
        #     "image":'image1',
        #     'sponsored': False,
        #     'description': "Arama USB Headset with Microphone Noise-Cancelling, Comfort Fit Computer Headset with Microphone for PC Laptop Mac Skype Zoom UC Webinar Business Call Center Home Office",
        #     "rating":"5 stars",
        #     'price': '$27.99',
        #     'coupon': '20%',
        #     'Delivery': 'Delivery Thu, Aug 17',
        #     'destination': 'Ghana',
        #     'total_rating': '1,298'
        # }]
        # print products shopping cart
        return render(request, template_name='products/products.html', context={'shop': shop_name,
                                # products in the specific category
                                'products': products})
    
class ProductDetailView(View):
    def get(self, request, shop_name, product_name):
        """Return a Template with the details of a product"""        
        product = Product.objects.get(name = product_name)

        # generate product specification information
        
        return render(request=request, template_name='products/product_details.html',
                      context={'shop': shop_name,
                                'details': product,
                                'thumbnails': [1,2,3,4],
                     })
