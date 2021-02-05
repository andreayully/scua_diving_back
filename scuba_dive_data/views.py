from django.shortcuts import render
from rest_framework import generics

from scuba_dive_data.models import ScubaDiveData
from scuba_diving_back.serializers import ScubaDiveDataSerializer


class ScubaDiveDataListCreateView(generics.ListCreateAPIView):
    """
    View for list and create scuba divie data
    GET: list of data
    POST: create new data
    """
    queryset = ScubaDiveData.objects.all()
    serializer_class = ScubaDiveDataSerializer
