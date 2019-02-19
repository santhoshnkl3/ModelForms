from django.db import models
from django.db.models import CharField,DateField,IntegerField

# Create your models here.
class AddVehicles(models.Model):
    vehicle_number=models.CharField(max_length=10)
    vehicle_insurance_dt=models.DateField()
    vehicle_fc_dt=models.DateField()
    vehicle_chasis_number=models.CharField(max_length=32)
    vehicle_engine_number=models.CharField(max_length=32)

    def __str__(self):
        return self.vehicle_number

        

class AddDriver(models.Model):
    driver_name=models.CharField(max_length=32)
    driver_address=models.CharField(max_length=100)
    driver_contact=models.IntegerField()
    driver_license_no=models.CharField(max_length=32)
    driver_license_exp_dt=models.DateField()

    def __str__(self):
        return self.driver_name
