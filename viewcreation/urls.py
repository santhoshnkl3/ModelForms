from django.urls import path
from . import views
urlpatterns=[
path('',views.add_vehicles,name='addvehicle'),
path('sucess/',views.sucess,name='sucess')

]
