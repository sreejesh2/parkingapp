from django import forms
from .models import Vehicles

class VehicleEntryForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = ['vehicle_num']

class VehicleExitForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = ['vehicle_num'] 