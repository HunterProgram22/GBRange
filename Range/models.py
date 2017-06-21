from django.db import models
from .constants import CENTERSTRIKE_EXPERIMENTAL_DRILLS, CENTERSTRIKE_TECH_AREAS, \
    PHASES, ALL_CLUBS, AREAS


class Drill_Base_Model(models.Model):
    area = models.CharField(max_length=50, choices=AREAS)
    phase = models.CharField(max_length=25, choices=PHASES)
    date = models.DateField()
    drill = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(blank=True, null=True)
    detail = models.CharField(max_length=100, blank=True)
    club = models.CharField(max_length=25, choices=ALL_CLUBS)
    shots_hit = models.IntegerField()
    shots_success = models.IntegerField(blank=True, null=True)
