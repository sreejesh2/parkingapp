from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import VehicleEntryForm, VehicleExitForm
from .models import Vehicles
# Create your views here.
def home(request):
    if request.method == 'POST':
        entry_form = VehicleEntryForm(request.POST)
        exit_form = VehicleExitForm(request.POST)

        if entry_form.is_valid():
            # Create or update the Vehicles instance for entry
            Vehicles.objects.update_or_create(
                vehicle_num=entry_form.cleaned_data['vehicle_num'],
                entry_time = timezone.now()
            )

        if exit_form.is_valid():
            # Create or update the Vehicles instance for exit
            Vehicles.objects.update_or_create(
                vehicle_num=exit_form.cleaned_data['vehicle_num'],
                exit_time = timezone.now()
            )

        # Redirect to avoid form resubmission on page refresh
        return redirect('home')

    else:
        entry_form = VehicleEntryForm()
        exit_form = VehicleExitForm()

    return render(request, 'home.html', {'entry_form': entry_form, 'exit_form': exit_form})