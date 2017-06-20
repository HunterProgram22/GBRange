# Clubs
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

WOOD_CLUBS = (
        (D1, 'Driver'),
        (D3, 'Three Wood'),
        )

HYBRID_CLUBS = (
        (H3, '3 Hybrid'),
        )

IRON_CLUBS = (
        (I5, '5 Iron'),
        (I6, '6 Iron'),
        (I7, '7 Iron'),
        (I8, '8 Iron'),
        (I9, '9 Iron'),
        )

WEDGE_CLUBS = (
        (PW, 'Pitching Wedge 45'),
        (GW, 'Gap Wedge 50'),
        (SW, 'Sand Wedge 54'),
        (LW, 'Lob Wedge 58'),
        )

CHIPPING_CLUBS = (
        (I9, '9 Iron'),
        (PW, 'Pitching Wedge 45'),
        (GW, 'Gap Wedge 50'),
        (SW, 'Sand Wedge 54'),
        (LW, 'Lob Wedge 58'),
        )


# Technical Skill Areas
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

CENTERSTRIKE_TECH_AREAS = (
        (CENTER_STRIKE, 'Center Face Hit'),
        (ANGLE_OF_ATTACK, 'Upward Angle of Attack'),
        (CLUB_FACE_PATH, 'Club Face and Path'),
        )


# Experimental Drills
HEEL_TOE = 'HTH'
THIN_FAT = 'TFH'
WEAK_STRONG = 'WSG'
THREE_INCH = '3IH'
TWO_INCH = '2IH'
RIGHT_ARM = 'RAC'

CENTERSTRIKE_EXPERIMENTAL_DRILLS = (
        (HEEL_TOE, 'Heel and Toe Hits'),
        (THIN_FAT, 'High and Low Face Hits'),
        (WEAK_STRONG, 'Weak and Strong Grip'),
        )
