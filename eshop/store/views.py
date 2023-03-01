from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    banners = Banner.objects.all()
    products = Product.objects.all()
    context ={
        'banners':banners,
        'products':products
    }
    return render(request, 'store/home.html', context)

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    product_image_gallery = ProductImageGallery.objects.filter(product=product)

    related_product = Product.objects.filter(category=product.category).exclude(pk=pk)

    context ={
        'product':product,
        'product_image_gallery':product_image_gallery,
        'related_product':related_product,
    }
    return render(request, 'store/product-detail.html', context)