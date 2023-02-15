from django import forms 
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'enter your name',
    }))
    phone  = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'enter your phone number',
    }))
    email  = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'enter your email',
    }))
    message  = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'enter your message',
    }))
    
    class Meta:
        model = Contact
        fields = '__all__'