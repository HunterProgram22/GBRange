from django.db import models
from .constants import CENTERSTRIKE_EXPERIMENTAL_DRILLS, CENTERSTRIKE_TECH_AREAS, \
    PHASES, ALL_CLUBS


class Drill_Base_Model(models.Model):
    date = models.DateField()
    phase = models.CharField(max_length=25, choices=PHASES)
    detail = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    drill = models.CharField(max_length=50)
    level = models.IntegerField()
    club = models.CharField(max_length=25, choices=ALL_CLUBS)
    shots_hit = models.IntegerField()
    shots_success = models.IntegerField()
