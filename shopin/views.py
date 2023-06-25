"""
    Module is tasked with handling the business
    logic for all the views that come to this site
    MY VIEW IS VERY NOISE WITH UNWANTED
"""
from django.shortcuts import render
from django.http import HttpResponse


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
        'Moto': 'Peace and Love'
    }, {
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto': 'Love over hate'
    }, {
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'The Future is yours'
    }, {
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'Be The Change'
    }, {
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'Shop Right'
    }, {
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto': 'Shoping Made Easy'
    }, {
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto': 'Making the sales'
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
    context = {'shop_list': list_of_shops,
               'top_rated': top_rated,
               'length':  # context to display to the home page
               [len(shop['Description']) for shop in list_of_shops]}
    return render(request, 'shopin/index.html', context=context)

# i will need a view to handle specific view of a shop

def view_a_shop(request, shop_id):

    SD_SHOP = 'A very simple shopin template for ' +\
        'show casing a description to be in the name of laughter'
    list_of_shops = [{
        'id': 1,
        'Title': 'Shopin 1',
        'Description': SD_SHOP + 'This is specific to ',
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'red',
        'Moto': 'Peace and Love',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : [{'name': 'first',
                                  'img': 'image1_url'},
                                 {'name': 'second',
                                  'img': 'image2_url'},
                                 {'name': 'third',
                                  'img': 'image3_url'},
                                 {'name': 'fourth',
                                  'img': 'image4_url'},
                                  {'name': 'fifth',
                                  'img': 'image5_url'}]
            },
            'second_cat': {
                'name': 'second_cat',
                'img': 'second_image_url'
            },
            'third_cat': {
                'name': 'third_cat',
                'img': 'third_img_url'
            },
            'fouth': {
                'name': 'fourth_cat',
                'img': 'fourth_image_url'
            },
            'fifth': {
                'name': 'fifth_cat',
                'img': 'fifth_image_url'  
            }
        }
    }, {
        'id': 2,
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Accra',
        'Rating': '4 stars',
        'Color': 'green',
        'Moto': 'Love over hate',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': 'furst_cat',
            'second_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'third_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'fourth_cat': ['cat1', 'cat2', 'cat3', 'cat4']
        }
    }, {
        'id': 3,
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tarkwa',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'The Future is yours',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'second_cat': 'second_cat',
            'third_cat': 'third_cat',
            'fourth_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            }
        }
    }, {
        'id': 4,
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'Be The Change',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'second_cat': 'second_cat',
            'third_cat': ['cat1', 'cat2', 'cat3', 'cat4'],
            'fourth_cat': 'Fourth_cat'
        }
    }, {
        'id': 5,
        'Title': 'Shopin 3',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'yellow',
        'Moto': 'Shop Right',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'second_cat': 'second_cat',
            'third_cat': ['cat1', 'cat2', 'cat3', 'cat4'],
            'fourth_cat': 'Fourth_cat'
        }
    }, {
        'id': 6,
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto': 'Shoping Made Easy',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'second_cat': 'second_cat',
            'third_cat': ['cat1', 'cat2', 'cat3', 'cat4'],
            'fourth_cat': 'Fourth_cat'
        }
    }, {
        'id': 7,
        'Title': 'Shopin 2',
        'Description': SD_SHOP,
        'Location': 'Tumu',
        'Rating': '5 stars',
        'Color': 'green',
        'Moto': 'Making the sales',
        'Category': {
            # inside this dictionary are categories
            # and the items that they can contain
            'first_cat': {
                'subsections' : ['first', 'second',
                                 'third', 'fourth',
                                 'fifth', 'sixth']
            },
            'second_cat': 'second_cat',
            'third_cat': ['cat1', 'cat2', 'cat3', 'cat4'],
            'fourth_cat': 'Fourth_cat'
        }
    }]
    """
        i'm gonna be doing a lot of
        complex operations
    """
    content = None
    if request.method == 'POST':
        print('post method accessed')
    
    elif request.method == 'GET':
        for shop in list_of_shops:
            if shop['id'] == int(shop_id):
                content = shop
    
    # i wanna perform some pre logic before 
    for category, value in content['Category'].items():
        print(f'value is: {value}')
        if 'subsections' in value:
            for section in value['subsections']:
                print(section)
        

    
    return render(request, 'shopin/shop_view.html', content)