from django.db import models

class Address(models.Model):
  #id = models.AutoField(primary_key=True)
  latitude=models.DecimalField(decimal_places=2, max_digits=65)
  longitude=models.DecimalField(decimal_places=2, max_digits=65)
  country=models.CharField(max_length=200)
  city=models.CharField(max_length=200)
  #barangay=models.CharField(max_length=200)