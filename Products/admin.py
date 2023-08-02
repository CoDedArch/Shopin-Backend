from django.contrib import admin
from .models import (Product, ShoppingCart, Order)
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

class ShoppingCartAdmin(admin.ModelAdmin):
    pass

class OrdersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Order, OrdersAdmin)
