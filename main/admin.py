from .models import Bestproduct, Category, Subcategory, Subcategory1, Brand, Automodel, Automodel1, Automodel2, Manufacturer, Product
from django.contrib import admin


# Register your models here.
class BestproductConfig(admin.ModelAdmin):
    fields = ('name', 'img', 'price', 'price_disc', 'new')
    list_display = ('name', 'price', 'date')


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description',)
    list_filter = ('category', 'subcategory', 'brand', 'manufacturer')


admin.site.register(Bestproduct, BestproductConfig)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Subcategory1)
admin.site.register(Brand)
admin.site.register(Automodel)
admin.site.register(Automodel1)
admin.site.register(Automodel2)
admin.site.register(Manufacturer)
