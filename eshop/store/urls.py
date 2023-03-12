from django.urls import path 
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
    path('product-filter/<pk>', categoryfiltering, name='category-filter'),
    path('product-search', product_search, name='product-search'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
    path('cart-summary', cart_summary, name='cart-summary'),
]