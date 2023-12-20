# views.py
from django.shortcuts import render, redirect
from .forms import VehicleEntryForm, VehicleExitForm
from .models import Vehicle,HourlyCharge
from django.utils import timezone

# views.py
from django.shortcuts import render, redirect
from .forms import VehicleEntryForm, VehicleExitForm
from .models import Vehicle
from django.utils import timezone

def home(request):
    if request.method == 'POST':
        if 'entry_form_submit' in request.POST:
            entry_form = VehicleEntryForm(request.POST)
            exit_form = VehicleExitForm()

            if entry_form.is_valid():
                vehicle_num = entry_form.cleaned_data['vehicle_num']
                entry_time = timezone.now()
                # Check if the vehicle with the given number is currently parked
                vehicle_instance = Vehicle.objects.filter(vehicle_num=vehicle_num, exit_time__isnull=True).first()

                if vehicle_instance:
                    # Handle the case where the vehicle is already parked
                    print("Vehicle is already parked")
                else:
                    # Create a new parking instance
                    Vehicle.objects.create(vehicle_num=vehicle_num, entry_time=entry_time)

        elif 'exit_form_submit' in request.POST:
            entry_form = VehicleEntryForm()
            exit_form = VehicleExitForm(request.POST)

            if exit_form.is_valid():
                vehicle_num = exit_form.cleaned_data['vehicle_num']
                exit_time = timezone.now()

                # Check if the vehicle with the given number is currently parked
                vehicle_instance = Vehicle.objects.filter(vehicle_num=vehicle_num, exit_time__isnull=True).first()

                if vehicle_instance:
                    # Calculate the parking duration and fee
                    parking_duration = exit_time - vehicle_instance.entry_time
                    cost_per_hour = HourlyCharge.objects.get(id=1)
                    parking_fee = (parking_duration.total_seconds() / 3600) * cost_per_hour
                    parking_fee = round(parking_fee, 2)

                    # Update the existing instance with the exit time and parking fee
                    vehicle_instance.exit_time = exit_time
                    vehicle_instance.parking_fee = parking_fee
                    vehicle_instance.save()

                    print("Parking Fee for this entry and exit:", parking_fee)
                else:
                    # Handle the case where the vehicle is not currently parked
                    print("Vehicle is not currently parked")

        return redirect('home')

    else:
        entry_form = VehicleEntryForm()
        exit_form = VehicleExitForm()

    return render(request, 'home.html', {'entry_form': entry_form, 'exit_form': exit_form})

