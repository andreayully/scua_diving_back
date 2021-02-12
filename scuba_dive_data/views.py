from rest_framework import generics, filters

from scuba_dive_data.models import ScubaDiveData
from scuba_dive_data.serializers import ScubaDiveDataSerializer


class ScubaDiveDataListCreateView(generics.ListCreateAPIView):
    """
    View for list and create scuba divie data
    GET: list of data
    POST: create new data
    """
    queryset = ScubaDiveData.objects.all()
    serializer_class = ScubaDiveDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['max_depth', 'time_bellow_surface', 'starting_ox_level', 'ending_ox_level', 'location', 'ts',
                     'outside_temp', 'water_temp']
