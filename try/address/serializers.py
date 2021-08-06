from rest_framework import serializers
from .models import Address

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model:Address
    fields=(
      'latitude', 
      'longitude',
      'country',
      'city', 
      'barangay'
    )