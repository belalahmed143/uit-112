from django.urls import path 
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
    path('product-filter/<pk>', categoryfiltering, name='category-filter'),
    path('product-search', product_search, name='product-search'),
]