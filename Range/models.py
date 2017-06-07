from django.db import models


D1 = "Driver"
D3 = "3 Wood"
H3 = "3 Hybrid"
I5 = "5 Iron"
I6 = "6 Iron"
I7 = "7 Iron"
I8 = "8 Iron"
I9 = "9 Iron"
PW = "Pitch Wedge 45"
GW = "Gap Wedge 50"
SW = "Sand Wedge 54"
LW = "Lob Wedge 58"
PT = "Putter"
CLUBS = (   (D1, "Driver"),
            (D3, "3 Wood"),
            (H3, "3 Hybrid"),
            (I5, "5 Iron"),
            (I6, "6 Iron"),
            (I7, "7 Iron"),
            (I8, "8 Iron"),
            (I9, "9 Iron"),
            (PW, "Pitch Wedge 45"),
            (GW, "Gap Wedge 50"),
            (SW, "Sand Wedge 54"),
            (LW, "Lob Wedge 58"),
            (PT, "Putter"),
            )


TECHNICAL = "Technical"
EXPERIMENTAL = "Experimental"
CALIBRATION = "Calibration"
PERFORMANCE = "Performance"
GAMES = "Routine and Games"
TEST = "Test"
PRACTICE_AREAS= (   (TECHNICAL, "Technical"),
                    (EXPERIMENTAL, "Experimental"),
                    (CALIBRATION, "Calibration"),
                    (PERFORMANCE, "Performance"),
                    (GAMES, "Routine and Games"),
                    (TEST, "Test"),
                    )




class Pass_Fail_Drill(models.Model):
    '''Maybe remove Pass_Fail_Drill and use Wood_Drills'''
    name = models.CharField(max_length=200)
    date = models.DateField()
    practice_area = models.CharField(max_length=25, choices=PRACTICE_AREAS,
                                        default=TECHNICAL)
    club = models.CharField(max_length=25, choices=CLUBS)
    balls_hit = models.IntegerField()
    balls_succesful = models.IntegerField()
