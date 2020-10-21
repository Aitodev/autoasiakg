from django.urls import path
from .views import *

appname = 'main'

urlpatterns = [
    path('', index, name='index'),
]