from django.shortcuts import render
from rest_framework import viewsets

from bike.models import Bike
from bike.serializers import BikeSerializer


# Create your views here.
class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
