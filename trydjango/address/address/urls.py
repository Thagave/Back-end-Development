from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import InfoApi, LocationApi
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('api/token/', obtain_auth_token),
  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls')),
  path('', views.index), 
  path('infoapi/', views.InfoApi.as_view(),name="infoapi"), 
  path('locateapi/', views.LocationApi.as_view(),name="locateapi")
]