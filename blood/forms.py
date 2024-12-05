# forms.py
from django import forms
from .models import BloodDonation

class DonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['name', 'email', 'phone', 'blood_type', 'donation_date', 'location', 'image', 'age', 'address']
