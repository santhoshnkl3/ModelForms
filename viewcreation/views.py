from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from .forms import Add_Vehicle
from .models import AddVehicles

def add_vehicles(request):
    if request.method=='POST':
        form=Add_Vehicle()
        vehicle_number=request.POST.get('vehicle_number')
        vehicle_insurance_dt=request.POST.get('vehicle_insurance_dt')
        vehicle_engine_number=request.POST.get('vehicle_engine_number')
        vehicle_chasis_number=request.POST.get('vehicle_chasis_number')
        vehicle_fc_dt=request.POST.get('vehicle_fc_dt')
        obj=AddVehicles(vehicle_fc_dt=vehicle_fc_dt,vehicle_number=vehicle_number,vehicle_insurance_dt=vehicle_insurance_dt,vehicle_chasis_number=vehicle_chasis_number,vehicle_engine_number=vehicle_engine_number)
        obj.save()
        return HttpResponse("Object Saved Sucessfully")
    else:
        form=Add_Vehicle()
        return render(request,"home.html",{'form':form})
def sucess(request):
    return HttpResponse("Registered Sucessfully")
