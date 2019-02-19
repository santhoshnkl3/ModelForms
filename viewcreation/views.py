from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from .forms import Add_Vehicle,Add_Driver
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
def add_driver(request):
    if request.method=='POST':
        form=Add_Driver()
        driver_name=request.POST.get('driver_name')
        driver_contact=request.POST.get('driver_contact')
        driver_license_no=request.POST.get('driver_license_no')
        driver_license_exp_dt=request.POST.get('driver_license_exp_dt')
        driver_address=request.POST.get('driver_address')
        obj1=Add_Driver(driver_name = driver_name,driver_address=driver_address,driver_contact=driver_contact,driver_license_no=driver_license_no,driver_license_exp_dt=driver_license_exp_dt)
        obj1.save()
        return HttpResponse('Driver Object Saved Sucessfully')
    else:
        form=Add_Driver()
        return render(request,"driver.html",{'form':form})


def sucess(request):
    return HttpResponse("Registered Sucessfully")
