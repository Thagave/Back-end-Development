from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Farm_Location, Farmer_Info
from .forms import LocateForm, InfoForm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import InfoSerializer, LocationSerializer


def index(request):
  info_form = InfoForm()
  locate_form = LocateForm()
  if request.method == 'POST':
    info_form = InfoForm(request.POST)
    locate_form = LocateForm(request.POST)
    if info_form.is_valid() and locate_form.is_valid():
        info_form.save()
        locate_form.save()
  context = {'info_form':info_form, 'locate_form':locate_form}
  return render(request, 'web/index.html', context)
      



class InfoApi(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request,*args,**kwargs):
    qs=Farmer_Info.objects.all()
    serializer=InfoSerializer(qs, many=True)
    #permission_classes = (IsAdminOrReadOnly)
    return Response(serializer.data)
  def post(self, request,*args,**kwargs):
    Serializer=InfoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
      return Response(serializer.errors)
     
class LocationApi(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request,*args,**kwargs):
    qs=Farm_Location.objects.all()
    serializer=LocationSerializer(qs, many=True)
    #permission_classes = (IsAdminOrReadOnly)
    return Response(serializer.data)
  def post(self, request,*args,**kwargs):
    Serializer=LocationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
      return Response(serializer.errors)