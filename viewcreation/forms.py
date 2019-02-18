from django import forms
from django.forms import CharField,IntegerField,DateField


class Add_Vehicle(forms.Form):
    vehicle_number=forms.CharField(max_length=10,label='exampleInputPassword1')
    vehicle_chasis_number=forms.CharField(max_length=32,label='exampleInputPassword1')
    vehicle_engine_number=forms.CharField(max_length=32,label='exampleInputPassword1')
    vehicle_insurance_dt=forms.DateField(label='exampleInputPassword1')
    vehicle_fc_dt=forms.DateField(label='exampleInputPassword1')
