from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = '__all__'