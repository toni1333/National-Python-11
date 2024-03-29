from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from aplicatie1.models import Location
from myapi.serializer import LocationSerializers


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializers

