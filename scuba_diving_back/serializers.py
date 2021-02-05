from rest_framework import serializers
from scuba_dive_data.models import ScubaDiveData


class ScubaDiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScubaDiveData
        fields = '__all__'
