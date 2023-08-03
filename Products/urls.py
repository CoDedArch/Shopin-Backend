from django.urls import re_path
from . import views as product_views
urlpatterns = [
    re_path(r'^$',view=product_views.ViewProducts.as_view(),name='all_products')
]