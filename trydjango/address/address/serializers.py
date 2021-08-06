from rest_framework import serializers
from .models import Farm_Location, Farmer_Info

class InfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farmer_Info
    fields = '__all__'
    
    
class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Farm_Location  
    fields = '__all__' 