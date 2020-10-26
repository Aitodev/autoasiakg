from django.urls import path
from .views import *

appname = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('products/', contact, name='contact'),
]
