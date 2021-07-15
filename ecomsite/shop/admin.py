from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "online shopping at your doorstep"
admin.site.index_title = "Manage Site"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

        
    list_display = ('title','price','discount_price','category')
    search_fields = ('title',)

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)