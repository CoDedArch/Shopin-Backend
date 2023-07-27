from django.contrib import admin
from .models import (Customer, Reviews)

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


class ReviewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Reviews, ReviewsAdmin)