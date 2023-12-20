# forms.py
from django import forms
from .models import Vehicle

class VehicleEntryForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_num']
        widgets = {'vehicle_num': forms.TextInput(attrs={'placeholder': 'Enter vehicle number'})}

class VehicleExitForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_num']
        widgets = {'vehicle_num': forms.TextInput(attrs={'placeholder': 'Enter vehicle number'})}
