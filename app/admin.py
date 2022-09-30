from django.contrib import admin
from app.models import (slider,banner_area,Main_Category,Category,
                        Sub_category,Section,Product, Product_Image
                        ,Additional_Information)
# Register your models here.


class Product_Images(admin.TabularInline):
    model= Product_Image
class Additional_Informations(admin.TabularInline):
    model= Additional_Information
    
class ProductAdmin(admin.ModelAdmin):
    inlines= (Product_Images, Additional_Informations)
    list_display=('product_name', 'price', 'Categories','section')
    prepopulated_fields = {'slug': ('product_name',)}
    
    
admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Sub_category)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
admin.site.register(Section)