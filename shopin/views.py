"""
    Module is tasked with handling the business
    logic for all the views that come to this site
"""
from django.shortcuts import render
from django.views import View
from .models import Shop


# Create your views here.
# def home_page(request):
#     """
#         Returns the home page for Shopin
#         Since this i will be loading a template
#         i will not be using an HttpResponse
#         but a render
#     """
#     # retrieve list of all shop in the database
#     list_of_shops = Shop.objects.all()
#     print(list_of_shops)
#     # get the top rated shops        

#     context = {'shop_list': list_of_shops,
#                'top_rated': Shop.randomly_fetch_three_top_rated(),
#                'length': 4
#     }
#     return render(request, 'shopin/index.html', context=context)

# # i will need a view to handle specific view of a shop


class ShopView(View):
    """The View of all shops associated with a User """
    def get(self, request):
        list_of_shops = Shop.objects.all()

        context = {
            'shop_list': list_of_shops,
            'top_rated': Shop.randomly_fetch_three_top_rated(),
            'length': 4}
        
        return render(request, template_name= 'shopin/index.html', context=context)

# def view_a_shop(request, shop_id):
#     """ displays everything about a shop and its related models"""

#     #query a for a shop with name coded
#     coded = Shop.objects.get(title = 'CoDed')
#     for section in coded.section_set.all():
#         if section.contains_category:
#             # print the name of the category
#             for section_category in section.category.all():
#                 print(section_category.name)
    


#     SD_SHOP = 'A very simple shopin template for ' +\
#         'show casing a description to be in the name of laughter'
#     list_of_shops = [{
#         'id': 1,
#         'Title': 'Shopin 1',
#         'Description': SD_SHOP + 'This is specific to ',
#         'Location': 'Tumu',
#         'Rating': '5 stars',
#         'Color': 'red',
#         'Moto': 'Peace and Love',
#         'Sections':{
#             # inside this dictionary are categories
#             # and the items that they can contain
#             'section1': {
#                 'Category': [{
#                     'first_cat': {
#                         'subsections': [{'name': 'first',
#                                         'img': 'image1_url'},
#                                         {'name': 'second',
#                                         'img': 'image2_url'},
#                                         {'name': 'third',
#                                         'img': 'image3_url'},
#                                         {'name': 'fourth',
#                                         'img': 'image4_url'},
#                                         {'name': 'fifth',
#                                         'img': 'image5_url'}]
#                     }},{
#                     'second_cat': {
#                         'name': 'second_cat',
#                         'img': 'second_image_url'
#                     }},{
#                     'third_cat': {
#                         'name': 'third_cat',
#                         'img': 'third_img_url'
#                     }},{
#                     'fouth': {
#                         'name': 'fourth_cat',
#                         'img': 'fourth_image_url'
#                     }},{
#                     'fifth': {
#                         'name': 'fifth_cat',
#                         'img': 'fifth_image_url'  
#                     }}
#                 ],
#                 'color': 'black',
#                 'status': {
#                     # meaning that i'll have to get the products of a section.
#                     'contains_only_products': False,
#                     'contains_category': True
#                 },
#                 'pagnation_unit': 5
#             },
#             'section2': {
#                 'Category': [{
#                     'first_cat': {
#                         'name':'',
#                         'img': 'third_urls'
#                      }},
#                     {'second_cat': {
#                         'subsections' : [{'name': 'first',
#                                         'img': 'image1_url'},
#                                         {'name': 'second',
#                                         'img': 'image2_url'},
#                                         {'name': 'third',
#                                         'img': 'image3_url'},
#                                         {'name': 'fourth',
#                                         'img': 'image4_url'},
#                                         {'name': 'fifth',
#                                         'img': 'image5_url'}]
#                     }},
#                     {'third_cat': {
#                         'subsections' : [{'name': 'first',
#                                         'img': 'image1_url'},
#                                         {'name': 'second',
#                                         'img': 'image2_url'},
#                                         {'name': 'third',
#                                         'img': 'image3_url'},
#                                         {'name': 'fourth',
#                                         'img': 'image4_url'},
#                                         {'name': 'fifth',
#                                         'img': 'image5_url'}]
#                     }},
#                     {'fourth_cat': ['cat1', 'cat2', 'cat3', 'cat4']
#                 }],
#                 'color': 'green',
#                 'status': {
#                     # meaning that i'll have to get the products of a section.
#                     'contains_only_products': False,
#                     'contains_category': True
#                 },
#                 'pagnation_unit': 1
#             },
#             'section3': {
#                 'status': {
#                     # meaning that i'll have to get the products of a section.
#                     'contains_only_products': True,
#                     'contains_category': False
#                 },
#                 'products': [{
#                     'img':'img_url',
#                     'offer': '25% off',
#                     'offer_name': 'Deal',
#                     'name': 'gown',
#                     'price': 'ghs 2000',
#                     'desc':'some long text which will be truncated'
#                 }, 'prod2_thumb', 'prod3_thumb',
#                     'prod4_thumb', 'prod5_thumb', 'prod5_thumb'],
#                 'section_title':'Under ghc300',
#                 'call_to_action':'see more',
#                 'pagnation_unit': 2
#             }
#         }
#     }, {
#         'id': 2,
#         'Title': 'Shopin 2',
#         'Description': SD_SHOP,
#         'Location': 'Accra',
#         'Rating': '4 stars',
#         'Color': 'green',
#         'Moto': 'Love over hate',
#         'Sections': {
#             # inside this dictionary are categories
#             # and the items that they can contain
#             'section1': {
#                 'Category': [{
#                     'first_cat': 'first_cat'},
#                     {'second_cat': {
#                         'subsections' : ['first', 'second',
#                                         'third', 'fourth',
#                                         'fifth', 'sixth']
#                     }},
#                     {'third_cat': {
#                         'subsections' : ['first', 'second',
#                                         'third', 'fourth',
#                                         'fifth', 'sixth']
#                     }},
#                     {'fourth_cat': ['cat1', 'cat2', 'cat3', 'cat4']
#                 }],
#                 'color': 'red',
#                 'status': {
#                     # meaning that i'll have to get the products of a section.
#                     'contains_only_products': False,
#                     'contains_category': True
#                 },
#                 'pagnation_unit': 3
#             },
#             'section2': {
#                 'Category': [{
#                     'first_cat': 'furst_cat'},
#                     {'second_cat': {
#                         'subsections' : ['first', 'second',
#                                         'third', 'fourth',
#                                         'fifth', 'sixth']
#                     }},
#                     {'third_cat': {
#                         'subsections' : ['first', 'second',
#                                         'third', 'fourth',
#                                         'fifth', 'sixth']
#                     }},
#                     {'fourth_cat': ['cat1', 'cat2', 'cat3', 'cat4']
#                 }],
#                 'color': 'green',
#                 'pagnation_unit': 4
#             },
#         }
#     }]
#     """
#         i'm gonna be doing a lot of
#         complex operations
#     """
#     content = None
#     if request.method == 'POST':
#         print('post method accessed') 
#     elif request.method == 'GET':
#         for shop in list_of_shops:
#             if shop['id'] == int(shop_id):
#                 content = shop
#     print(content)
#     for section, section_value in content['Sections'].items():
#         if section_value['status']['contains_category']:
#             for category in section_value['Category']:
#                 print(category)
    # i wanna perform some pre logic before 
    # return render(request, 'shopin/shop_view.html', content)

class SingleShopView(View):
    """Display the details of a single shop instance"""
    def get(self, request, shop_id):
        # retrieve the particular shop id
        # try:
        shop = Shop.objects.get(title = "CoDed")
        section = shop.section_set.all()
        for sec in section:
            print(sec.category_set.all())
            # if sec.contains_category:
            #     for category in sec.category.all():
            #         print(category)
                    # if category.wants_subcategory:
                    #     for subcat in category.subcategory_set.all():
                    #         print(subcat)
        # except: 
        #     print('shop id %s not found in db'% shop_id)
        return render(request=request, template_name='shopin/single_shopview.html', 
                      context= {'content': shop})
