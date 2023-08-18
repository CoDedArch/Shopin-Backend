from django.urls import re_path, path
from . import views as product_views
urlpatterns = [
    re_path(r'^(?P<category>\w+)/$',view=product_views.ViewCategoryProducts.as_view(),name='all_products'),
    re_path(r'^products/(?P<product_name>\w+)/$', view=product_views.ProductDetailView.as_view(), name='details')    
]