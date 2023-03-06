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
    