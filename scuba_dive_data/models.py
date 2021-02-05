from django.db import models
from django.utils import timezone


# Create your models here.


class ScubaDiveData(models.Model):
    """
    Model for the scuba dive data
    """
    max_depth = models.FloatField()
    time_bellow_surface = models.TimeField()
    starting_ox_level = models.FloatField()
    ending_ox_level = models.FloatField()
    location = models.CharField(max_length=100)
    ts = models.DateTimeField(default=timezone.now)
    outside_temp = models.FloatField()
    water_temp = models.FloatField()
    description = models.TextField()
