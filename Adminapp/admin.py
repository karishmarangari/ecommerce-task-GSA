from django.contrib import admin
from . models import Product, MyCart

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "p_name", "price", "description", "quantity", "image", "details")


class MyCartAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "qty")


admin.site.register(Product, ProductAdmin)
admin.site.register(MyCart, MyCartAdmin)
