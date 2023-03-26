from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
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

@login_required
def add_to_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created =CartProduct.objects.get_or_create(product=product,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
           cart_item.quantity += 1
           cart_item.save()
           messages.success(request,'this product quantity update')
           return redirect('product-detail',pk=product.pk)
        else:
            order.products.add(cart_item)
            messages.info(request,'this product was add to cart')
            return redirect('product-detail',pk=product.pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(cart_item)
        messages.info(request,'this product was add to cart')
        return redirect('product-detail',pk=product.pk)

@login_required
def cart_summary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)

        context ={
            'order':order
        }
        return render(request, 'store/cart-summary.html',context)
    except ObjectDoesNotExist:
        messages.info(request,'your cart is empty')
        return redirect('/')

@login_required
def quantity_increment(request,pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created =CartProduct.objects.get_or_create(product=product,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
           cart_item.quantity += 1
           cart_item.save()
           messages.info(request,'this product quantity update')
           return redirect('cart-summary')
    else:
        return redirect('cart-summary')

@login_required
def quantity_decrement(request,pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created =CartProduct.objects.get_or_create(product=product,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.info(request,'this product quantity update')
                return redirect('cart-summary')
            else:
                cart_item.delete()
                messages.info(request,'this product was delete')
                return redirect('cart-summary')
        else:
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')

@login_required
def remove_from_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created =CartProduct.objects.get_or_create(product=product,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__pk=product.pk).exists():
            cart_item.delete()
            messages.info(request,'this product was delete')
            return redirect('cart-summary')
        else:
            messages.info(request,'this product was not your cart')
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')


from django.views import View
from .forms import *

# 1st method

# class CheckoutView(View):
#     def get(self,request, *args, **kwargs):
#         try:
#             order = Order.objects.get(user=request.user, ordered=False)
#             form = CheckoutForm()
#             payment_method = PaymentMethodForm()
#             context ={
#                 'order':order,
#                 'form':form,
#                 'payment_method':payment_method

#             }
#             return render(request, 'store/checkout.html',context)
#         except ObjectDoesNotExist:
#             messages.info(request,'your cart is empty')
#             return redirect('/')

#     def post(self,request, *args, **kwargs):
#         form = CheckoutForm(request.POST)
#         payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
#         payment_form = PaymentMethodForm(instance=payment_obj)

#         if request.method == 'POST':
#             form = CheckoutForm(request.POST)
#             pay_form = PaymentMethodForm(request.POST,instance=payment_obj)

#             if form.is_valid() and pay_form.is_valid():
#                 full_address  =form.cleaned_data.get('full_address')
#                 phone =form.cleaned_data.get('phone')
#                 email =form.cleaned_data.get('email')
#                 order_note =form.cleaned_data.get('order_note')

#                 shippingAddress = Checkout(
#                     user = request.user,
#                     full_address = full_address,
#                     phone = phone,
#                     email = email,
#                     order_note = order_note
#                 )

#                 shippingAddress.save()
#                 payment_obj.shipping_address = shippingAddress
#                 pay_method = pay_form.save()

#                 if pay_method.payment_option == 'cash on delivery':
#                     order_qs = Order.objects.filter(user=request.user, ordered=False)
#                     order = order_qs[0]
#                     order.ordered = True
#                     order.payment_option = pay_method.payment_option
                    
#                     cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
#                     for cart_product in cart_products:
#                         cart_product.ordered = True
#                         cart_product.save()
#                     order.save()
#                     return redirect('/')


class CheckoutView(View):
    def get(self,request, *args, **kwargs):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            form = CheckoutForm()
            payment_method = PaymentMethodForm()
            context ={
                'order':order,
                'form':form,
                'payment_method':payment_method

            }
            return render(request, 'store/checkout.html',context)
        except ObjectDoesNotExist:
            messages.info(request,'your cart is empty')
            return redirect('/')

    def post(self,request, *args, **kwargs):
        form = CheckoutForm(request.POST)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)

        if request.method == 'POST':
            form = CheckoutForm(request.POST)
            pay_form = PaymentMethodForm(request.POST,instance=payment_obj)

            if form.is_valid() and pay_form.is_valid():
                form.instance.user = request.user
                shippingAddress = form.save()
                payment_obj.shipping_address = shippingAddress
                pay_method = pay_form.save()

                if pay_method.payment_option == 'cash on delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.payment_option = pay_method.payment_option
                    
                    cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
                    for cart_product in cart_products:
                        cart_product.ordered = True
                        cart_product.save()
                    order.save()
                    return redirect('/')

import requests
import json

base_url = 'https://checkout.sandbox.bka.sh/v1.2.0-beta'
app_key = "5nej5keguopj928ekcj3dne8p"
app_secret = "1honf6u1c56mqcivtc9ffl960slp4v2756jle5925nbooa46ch62"


def grant_token():
    url = f'{base_url}/checkout/token/grant'

    payload = {
    "app_key":f"{app_key}",
    "app_secret":f"{app_secret}"
    }

    headers = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "username":"testdemo",
        "password":"test%#de23@msdao"
    }

    token_respons = requests.post(url, json=payload,headers=headers)

    respons = json.loads(token_respons.content)
    id_token = respons['id_token']
    # print(id_token)
    # print(type(respons))

    return id_token

id_token =grant_token()
print(id_token)

from django.http import JsonResponse

@login_required
@csrf_exempt
def create_bkash_payment(request, *args, **kwargs):
    url = f'{base_url}/checkout/payment/create'

    payload = json.dumps({
        "amount":"505",
        "currency": "BDT",
        "intent": "sale",
        "merchantInvoiceNumber":"66jhbfdjs",
    })

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{id_token}",
        "X-APP-Key":f"{app_key}"   
    }

    create_response = requests.post(url,data=payload,headers=headers)

    response = json.loads(create_response.content)
    paymentID = response['paymentID']

    CreateBkash.objects.create(user=request.user,paymentID=paymentID)
    return JsonResponse(response)

@csrf_exempt
def execute_baksh(request):
    ID = CreateBkash.objects.filter(user=request.user).last()
    paymentID = ID.paymentID

    url = f'{base_url}/checkout/payment/execute/{paymentID}'

    headers = {
        "accept": "application/json",
        "Authorization": f"{id_token}",
        "X-APP-Key": "5nej5keguopj928ekcj3dne8p"
    }

    execute_response = requests.post(url,headers=headers)

    response = json.loads(execute_response.content)

    print(response)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    order.ordered = True
    order.payment_option = 'bkash'
    
    cart_products = CartProduct.objects.filter(user=request.user, ordered=False)
    for cart_product in cart_products:
        cart_product.ordered = True
        cart_product.save()
    order.save()

    return JsonResponse(response)




@login_required
def order_summary(request):
    try:
        order = Order.objects.filter(user=request.user, ordered=True)
        context ={
            'order':order
        }
        return render(request, 'store/order-summary.html',context)
    except ObjectDoesNotExist:
        messages.info(request,'your order is empty')
        return redirect('/')

def order_details(request,pk):
    order = Order.objects.get(pk=pk)
    # order_product = CartProduct.objects.all(order=order)

    context ={
            'order':order,

        }
    return render(request, 'store/order-details.html',context)