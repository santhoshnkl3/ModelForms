from django.db import models

# Create your models here.
class AddVehicles(models.Model):
    vehicle_number=models.CharField(max_length=10)
    vehicle_insurance_dt=models.DateField()
    vehicle_fc_dt=models.DateField()
    vehicle_chasis_number=models.CharField(max_length=32)
    vehicle_engine_number=models.CharField(max_length=32)

    def __str__(self):
        return self.vehicle_number
