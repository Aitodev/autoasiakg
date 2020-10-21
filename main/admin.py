from django.contrib import admin
from .models import Bestproduct

# Register your models here.
class BestproductConfig(admin.ModelAdmin):
    fields = ('name',  'img', 'price', 'price_disc', 'new')
    list_display = ('name', 'price', 'date')

admin.site.register(Bestproduct, BestproductConfig)
