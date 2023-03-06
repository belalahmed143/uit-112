from django.shortcuts import render,get_object_or_404
from .models import *
from django.db.models import Q


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

def categoryfiltering(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    products  = Product.objects.filter(Q(category=cate.pk) | Q(category__parent_category=cate.pk))

    context ={
       'cate':cate,
        'products':products,
    }
    return render(request, 'store/category-filtering.html', context)


def product_search(request):
    query = request.GET['q']
    lookups = Q(name__icontains=query) | Q(category__name__icontains=query) | Q(price__icontains=query) | Q(discount_price__icontains=query)
    products = Product.objects.filter(lookups)

    context ={
        'query':query,
        'products':products,
    }
    return render(request, 'store/search.html', context)