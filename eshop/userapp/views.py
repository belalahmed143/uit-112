from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Create')
            return redirect('/')
        else:
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'userapp/registration.html', {'form':form})

def profile(request):
    return render(request, 'userapp/profile.html')

def profileUpdate(request):
    if request.method == 'POST':
        reg_form = UpdateRegistrationForm(request.POST, instance=request.user)
        pro_form = UpdateProfileForm(request.POST, request.FILES ,instance=request.user.profile)
        if reg_form.is_valid() and pro_form.is_valid():
            reg_form.save()
            pro_form.save()
            messages.success(request, 'Account Create')
            return redirect('profile')
    else:
        reg_form = UpdateRegistrationForm(instance=request.user)
        pro_form = UpdateProfileForm(instance=request.user.profile)

    context ={
        'reg_form':reg_form,
        'pro_form':pro_form
    }
    return render(request, 'userapp/profile-update.html',context)
    