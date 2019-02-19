from django import forms
from django.forms import CharField,IntegerField,DateField


class Add_Vehicle(forms.Form):
    vehicle_number=forms.CharField(max_length=10)
    vehicle_chasis_number=forms.CharField(max_length=32)
    vehicle_engine_number=forms.CharField(max_length=32)
    vehicle_insurance_dt=forms.DateField()
    vehicle_fc_dt=forms.DateField()

class Add_Driver(forms.Form):
    driver_name=forms.CharField(max_length=32)
    driver_contact=forms.IntegerField()
    driver_license_no=forms.CharField(max_length=32)
    driver_license_exp_dt=forms.DateField()
    driver_address=forms.CharField(max_length=100)
