from django.contrib import admin
from .models import Vehicle,HourlyCharge
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(HourlyCharge)