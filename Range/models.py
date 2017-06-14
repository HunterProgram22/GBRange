from django.db import models

# Abstract Club Models
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

class Wood_Clubs(models.Model):
    WOOD_CLUBS = (
            (D1, 'Driver'),
            (D3, 'Three Wood'),
            )
    club = models.CharField(max_length=15, choices=WOOD_CLUBS)

    class Meta:
        abstract = True

class Hybrid_Clubs(models.Model):
    HYBRID_CLUBS = (
                    (H3, '3 Hybrid'),
                )
    club = models.CharField(max_length=15, choices=HYBRID_CLUBS)

    class Meta:
        abstract = True

class Iron_Clubs(models.Model):
    IRON_CLUBS = (
                (I5, '5 Iron'),
                (I6, '6 Iron'),
                (I7, '7 Iron'),
                (I8, '8 Iron'),
                (I9, '9 Iron'),
            )
    club = models.CharField(max_length=15, choices=IRON_CLUBS)

    class Meta:
        abstract = True

class Wedge_Clubs(models.Model):
    WEDGE_CLUBS = (
                (PW, 'Pitching Wedge 45'),
                (GW, 'Gap Wedge 50'),
                (SW, 'Sand Wedge 54'),
                (LW, 'Lob Wedge 58'),
            )
    club = models.CharField(max_length=20, choices=WEDGE_CLUBS)

    class Meta:
        abstract = True

class Chipping_Clubs(models.Model):
    CHIPPING_CLUBS = (
                (I9, '9 Iron'),
                (PW, 'Pitching Wedge 45'),
                (GW, 'Gap Wedge 50'),
                (SW, 'Sand Wedge 54'),
                (LW, 'Lob Wedge 58'),
            )
    club = models.CharField(max_length=20, choices=CHIPPING_CLUBS)

    class Meta:
        abstract = True

# Abstract Technical Models
CENTER_STRIKE = 'CS'
ANGLE_OF_ATTACK = 'AA'
CLUB_FACE_PATH = 'CP'
DIVOT_LOCATION = 'DL'
WEDGE_DIRECTION = 'WX'
WEDGE_DISTANCE = 'WD'
CHIPPING_DIRECTION = 'CX'
CHIPPING_DISTANCE = 'CD'
SPEED = 'PS'
PUTTING_LINE = 'PL'

class Technical_Drills(models.Model):
    date = models.DateField()
    detail = models.CharField(max_length=100)
    level = models.IntegerField()
    shots_hit = models.IntegerField()
    shots_success = models.IntegerField()

    class Meta:
        abstract = True


# Experimental Drills
HEEL_TOE = 'HTH'
THIN_FAT = 'TFH'
WEAK_STRONG = 'WSG'
THREE_INCH = '3IH'
TWO_INCH = '2IH'

class Experimental_Drills(models.Model):
    date = models.DateField()
    detail = models.CharField(max_length=100)
    shots_hit = models.IntegerField()

    class Meta:
        abstract = True


# Woods Models
class Woods_Experimental(Experimental_Drills, Wood_Clubs):
    DRILL_CHOICES = (
                (HEEL_TOE, 'Heel and Toe Hits'),
                (THIN_FAT, 'High and Low Face Hits'),
                (WEAK_STRONG, 'Weak and Strong Grip'),
    )
    drill = models.CharField(max_length=50, choices=DRILL_CHOICES)

class Woods_Technical(Technical_Drills, Wood_Clubs):
    TECH_CHOICES = (
                (CENTER_STRIKE, 'Center Face Hit'),
                (ANGLE_OF_ATTACK, 'Upward Angle of Attack'),
                (CLUB_FACE_PATH, 'Club Face and Path'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)


# Hybrids Models
class Hybrids_Technical(Technical_Drills, Hybrid_Clubs):
    TECH_CHOICES = (
                (CENTER_STRIKE, 'Center Face Hit'),
                (DIVOT_LOCATION, 'Divot Location'),
                (CLUB_FACE_PATH, 'Club Face and Path'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)


# Irons Models
class Irons_Technical(Technical_Drills, Iron_Clubs):
    TECH_CHOICES = (
                (CENTER_STRIKE, 'Center Face Hit'),
                (DIVOT_LOCATION, 'Divot Location'),
                (CLUB_FACE_PATH, 'Club Face and Path'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)


# Wedge Models
class Wedges_Technical(Technical_Drills, Wedge_Clubs):
    TECH_CHOICES = (
                (CENTER_STRIKE, 'Center Face Hit'),
                (WEDGE_DIRECTION, 'Wedge Direction'),
                (WEDGE_DISTANCE, 'Wedge Distance'),
                (DIVOT_LOCATION, 'Divot Location'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)

class Wedges_Experimental(Experimental_Drills, Wedge_Clubs):
    DRILL_CHOICES = (
                (HEEL_TOE, 'Heel and Toe Hits'),
                (THIN_FAT, 'High and Low Face Hits'),
                (WEAK_STRONG, 'Weak and Strong Grip'),
    )
    drill = models.CharField(max_length=50, choices=DRILL_CHOICES)


# Chipping Models
class Chipping_Technical(Technical_Drills, Chipping_Clubs):
    TECH_CHOICES = (
                (CENTER_STRIKE, 'Center Face Hit'),
                (CHIPPING_DIRECTION, 'Chipping Direction'),
                (CHIPPING_DISTANCE, 'Chipping Distance'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)


# Putting Models
class Putting_Technical(Technical_Drills):
    TECH_CHOICES = (
                (SPEED, 'Putting Speed'),
                (PUTTING_LINE, 'Putting Line'),
            )
    area = models.CharField(max_length=50, choices=TECH_CHOICES)

class Putting_Experimental(Experimental_Drills):
    DRILL_CHOICES = (
                (HEEL_TOE, 'Heel and Toe Hits'),
                (THREE_INCH, 'Hit to 3 Inch Hole'),
                (TWO_INCH, 'Hit to 2 Inch Hole'),
    )
    drill = models.CharField(max_length=50, choices=DRILL_CHOICES)




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
