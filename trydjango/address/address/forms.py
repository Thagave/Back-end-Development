from django.forms import ModelForm
from .models import Farm_Location, Farmer_Info


class InfoForm(ModelForm):
  class Meta:
    model = Farmer_Info
    fields = '__all__'
    
class LocateForm(ModelForm):
  class Meta:
    model = Farm_Location
    fields = '__all__'
    #fields = ['farm_latitude','farm_longitude','country','city','barangay']