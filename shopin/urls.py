"""
    Urls patterns specific to shopin app
    These urls are included in the main url confi
"""
from django.urls import re_path
from shopin import views as shopin_views
urlpatterns = [
    re_path(r'^$', shopin_views.ShopView.as_view(), name='shop'),
    re_path(r'^(?P<shop_id>\d+)/$', shopin_views.view_a_shop, name='shop')
]
