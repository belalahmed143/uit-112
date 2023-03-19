from django import forms
from .models import *

# class CheckoutForm(forms.Form):
#     full_address  = forms.CharField(max_length = 250)
#     phone  = forms.CharField(max_length = 150)
#     email  = forms.EmailField()
#     order_note  = forms.CharField()

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'
        exclude = ('user',)



Payment_Method = (
    ('cash on delivery','cash on delivery'),
    ('sslcmrz','sslcmrz'),    
)

class PaymentMethodForm(forms.ModelForm):
    payment_option  = forms.ChoiceField(choices=Payment_Method,widget=forms.RadioSelect(attrs={
        'class':'collapsed'
    }))

    class Meta:
        model = Order
        fields = ['payment_option']



