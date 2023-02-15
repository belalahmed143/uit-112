from django.shortcuts import render,redirect
from .models import Product
from .forms import ContactForm

# Create your views here.

def home(request):
    # products = Product.objects.all()[:4]
    # products = Product.objects.all().order_by('-id')
    # products = Product.objects.all().order_by('?')
    # products = Product.objects.all().order_by('-id')[:1]

    # products = Product.objects.filter(title__exact='Product-2')
    # products = Product.objects.filter(title__iexact='PrOduct-2')
    # products = Product.objects.filter(title__contains='p')
    # products = Product.objects.filter(description__in=['sadddfs'])
    # products = Product.objects.filter(category__name='cate-2')

    # context ={
    #     'products':products
    #     }
    
    return render(request, 'uit_app/home.html')

def about(request):

    return render(request, 'uit_app/about.html')

def contact(request):   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ContactForm()
            return redirect('contact')
    else:
        form = ContactForm()
    context ={
        'form':form
    }
    return render(request, 'uit_app/contact.html',context)
    
    
