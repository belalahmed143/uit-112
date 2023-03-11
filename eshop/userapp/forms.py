from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        fields =['username', 'email', 'first_name', 'last_name']

class UpdateRegistrationForm(forms.ModelForm):
    class Meta:
        model = User 
        fields =['username', 'email', 'first_name', 'last_name']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = '__all__'
        exclude =('user',)