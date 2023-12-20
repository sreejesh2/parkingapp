
from django.db import models

class Vehicle(models.Model):
    vehicle_num = models.CharField(max_length=20)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    parking_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.vehicle_num

class HourlyCharge(models.Model):
    cost_per_hour = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Hourly Charge: {self.cost_per_hour}'