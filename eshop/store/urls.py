from django.urls import path 
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('product-detail/<pk>', product_detail, name='product-detail')
]