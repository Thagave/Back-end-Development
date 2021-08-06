from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import PostSerializer
from .forms import AddressForm
from .models import Address


def address(request):
  print(request.user)
  form=AddressForm()
  if request.method=='POST':
    form=AddressForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Submitted')   
    return redirect('/address')
  return render(request,'address.html',{'form':form})
 

class GetApi(APIView):
  def get(self, request,args,kwargs):
    qs=Address.objects.all()
    serializer=PostSerializer(qs, many=True)
    return Response(serializer.data)
  def post(self, request,args,kwargs):
    Serializer=PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)