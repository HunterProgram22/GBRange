from django.db import models
from .constants import WOOD_CLUBS, HYBRID_CLUBS, IRON_CLUBS, WEDGE_CLUBS, \
    CHIPPING_CLUBS, CENTERSTRIKE_EXPERIMENTAL_DRILLS, CENTERSTRIKE_TECH_AREAS

# Club Models
class Wood_Clubs(models.Model):
    club = models.CharField(max_length=25, choices=WOOD_CLUBS)

    class Meta:
        abstract = True

class Hybrid_Clubs(models.Model):
    club = models.CharField(max_length=25, choices=HYBRID_CLUBS)

    class Meta:
        abstract = True

class Iron_Clubs(models.Model):
    club = models.CharField(max_length=25, choices=IRON_CLUBS)

    class Meta:
        abstract = True

class Wedge_Clubs(models.Model):
    club = models.CharField(max_length=25, choices=WEDGE_CLUBS)

    class Meta:
        abstract = True

class Chipping_Clubs(models.Model):
    club = models.CharField(max_length=25, choices=CHIPPING_CLUBS)

    class Meta:
        abstract = True


# Abstract Models
class Drill_Base_Model(models.Model):
    date = models.DateField()
    detail = models.CharField(max_length=100)
    shots_hit = models.IntegerField()

    class Meta:
        abstract = True

class Technical_Drills(Drill_Base_Model):
    level = models.IntegerField()
    shots_success = models.IntegerField()

    class Meta:
        abstract = True


# Drill Models
class Woods_Experimental(Drill_Base_Model, Wood_Clubs):
    drill = models.CharField(max_length=50, choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)

class Woods_Technical(Technical_Drills, Wood_Clubs):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Woods_Test(models.Model):
    pass

class Hybrids_Experimental(Drill_Base_Model, Hybrid_Clubs):
    drill = models.CharField(max_length=50, choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)

class Hybrids_Technical(Technical_Drills, Hybrid_Clubs):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Irons_Technical(Technical_Drills, Iron_Clubs):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Irons_Experimental(Drill_Base_Model, Iron_Clubs):
    drill = models.CharField(max_length=50,choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)

class Wedges_Technical(Technical_Drills, Wedge_Clubs):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Wedges_Experimental(Drill_Base_Model, Wedge_Clubs):
    drill = models.CharField(max_length=50, choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)

class Chipping_Experimental(Drill_Base_Model, Chipping_Clubs):
    drill = models.CharField(max_length=50, choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)

class Chipping_Technical(Technical_Drills, Chipping_Clubs):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Putting_Technical(Technical_Drills):
    area = models.CharField(max_length=50, choices=CENTERSTRIKE_TECH_AREAS)

class Putting_Experimental(Drill_Base_Model):
    drill = models.CharField(max_length=50, choices=CENTERSTRIKE_EXPERIMENTAL_DRILLS)
