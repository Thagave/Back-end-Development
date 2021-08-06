from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from address import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')), 
    path('', views.address),
    path('admin/', admin.site.urls),
    
]