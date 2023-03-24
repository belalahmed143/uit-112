from django.urls import path 
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('product-detail/<pk>', product_detail, name='product-detail'),
    path('product-filter/<pk>', categoryfiltering, name='category-filter'),
    path('product-search', product_search, name='product-search'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
    path('cart-summary', cart_summary, name='cart-summary'),
    path('quantity_increment/<pk>', quantity_increment, name='quantity_increment'),
    path('quantity_decrement/<pk>', quantity_decrement, name='quantity_decrement'),
    path('remove_from_cart/<pk>', remove_from_cart, name='remove_from_cart'),
    path('checkout', CheckoutView.as_view(),name='checkout'),


    path('create_bkash_payment',create_bkash_payment, name='create_bkash_payment'),
    path('execute_baksh',execute_baksh, name='execute_baksh'),
    
]