from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('brand', 'serialno', 'description')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('brand', 'serialno', 'description')


class MobileForm(forms.ModelForm):
    class Meta:  
        model = Mobile
        fields = ('brand', 'serialno', 'description')
