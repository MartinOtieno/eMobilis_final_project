# forms.py
from django import forms
from .models import BloodDonation
from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['name', 'email', 'phone', 'blood_type', 'donation_date', 'location', 'image', 'age', 'address']
        
class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
