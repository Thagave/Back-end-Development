from django.db import models
from django.contrib.auth.models import User


class Farmer_Info(models.Model):
  
  id = models.AutoField(primary_key=True)
  first_name= models.CharField(max_length=200)
  last_name= models.CharField(max_length=200)
  user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
  
  def __str__(self):
      return  self.first_name + " " + self.last_name
      
    
class Farm_Location(models.Model):
  
  farm_latitude = models.DecimalField(decimal_places=2, max_digits=65)
  farm_longitude = models.DecimalField(decimal_places=2, max_digits=65)
  country = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  barangay = models.CharField(max_length=200)
  owner = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
  def __str__(self):
      return str(self.owner)