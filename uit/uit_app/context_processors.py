from .models import *

def product(request):
    products = Product.objects.filter(category__name='cate-2')

    context = {
        'products':products
    }
    return context