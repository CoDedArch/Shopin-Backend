from django.contrib import admin
from .models import (Product, ShoppingCart, Order, Brand, Coupon)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

class ShoppingCartAdmin(admin.ModelAdmin):
    pass

class OrdersAdmin(admin.ModelAdmin):
    pass

class BrandAdmin(admin.ModelAdmin):
    pass

class CouponAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Coupon, CouponAdmin)