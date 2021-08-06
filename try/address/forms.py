from django.forms import ModelForm
from .models import Address

class AddressForm(ModelForm):
  class Meta:
    model=Address
    fields=('latitude','longitude','country','city')