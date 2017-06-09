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


class Woods_Technical(models.Model):
    CENTER_STRIKE = 'CS'
    ANGLE_OF_ATTACK = 'AA'
    CLUB_FACE_PATH = 'CP'
    WOODS_TECH_CHOICES = (
        (CENTER_STRIKE, 'Center Face Hit'),
        (ANGLE_OF_ATTACK, 'Upward Angle of Attack'),
        (CLUB_FACE_PATH, 'Club Face and Path'),
    )
    date = models.DateField()
    area = models.CharField(max_length=50, choices=WOODS_TECH_CHOICES)
    detail = models.CharField(max_length=100)
    level = models.IntegerField()
    shots_hit = models.IntegerField()
    shots_success = models.IntegerField()

class Woods_Test(models.Model):
    TOE_HIT = 'TH'
    CENTER_HIT = 'CH'
    HEEL_HIT = 'HH'
    CENTER_STRIKE_CHOICES = (
        (TOE_HIT, 'Toe Hit'),
        (CENTER_HIT, 'Center Hit'),
        (HEEL_HIT, 'Heel Hit'),
    )
    UP_ANGLE = 'UA'
    LEVEL_ANGLE = 'LA'
    DOWN_ANGLE = 'DA'
    ANGLE_OF_ATTACK_CHOICES = (
        (UP_ANGLE, 'Up Angle Hit'),
        (LEVEL_ANGLE, 'Flat Angle Hit'),
        (DOWN_ANGLE, 'Downward Angle Hit'),
    )
    MIDDLE_SHOT = 'MS'
    HOOK_SHOT = 'HS'
    SLICE_SHOT = 'SS'
    CLUB_FACE_PATH_CHOICES = (
            (MIDDLE_SHOT, 'Straight Shot'),
            (HOOK_SHOT, 'Hook Shot'),
            (SLICE_SHOT, 'Slice Shot'),
        )
    date = models.DateField()
    balls_hit = models.IntegerField(default=20)
    center_strike = models.CharField(
        max_length=15,
        choices=CENTER_STRIKE_CHOICES,
        )
    angle_of_attack = models.CharField(
        max_length=15,
        choices=ANGLE_OF_ATTACK_CHOICES,
        )
    club_face_path = models.CharField(
        max_length=15,
        choices=CLUB_FACE_PATH_CHOICES,
        )
