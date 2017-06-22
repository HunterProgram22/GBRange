# Phases
TE = "Testing"
DT = "Direct Technical"
EX = "Experimental"
CL = "Calibration"
PF = "Performance"
RG = "Routine and Games"

PHASES = (
    (TE, "Testing"),
    (DT, "Direct Technical"),
    (EX, "Experimental"),
    (CL, "Calibration"),
    (PF, "Performance"),
    (RG, "Routine and Games"),
    )

# Areas
WD = "Woods"
HY = "Hybrids"
IR = "Irons"
WE = "Wedges"
CH = "Chipping"
PT = "Putting"

AREAS = (
    (WD, "Woods"),
    (HY, "Hybrids"),
    (IR, "Irons"),
    (WE, "Wedges"),
    (CH, "Chipping"),
    (PT, "Putting"),
    )

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

ALL_CLUBS = (
        (D1, 'Driver'),
        (D3, 'Three Wood'),
        (H3, '3 Hybrid'),
        (I5, '5 Iron'),
        (I6, '6 Iron'),
        (I7, '7 Iron'),
        (I8, '8 Iron'),
        (I9, '9 Iron'),
        (PW, 'Pitching Wedge 45'),
        (GW, 'Gap Wedge 50'),
        (SW, 'Sand Wedge 54'),
        (LW, 'Lob Wedge 58'),
        (PT, 'Putter'),
    )

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

DRILLS = (
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

WOOD_EXPERIMENTAL_DRILLS = (
        (HEEL_TOE, 'Heel and Toe Hits'),
        (THIN_FAT, 'High and Low Face Hits'),
        (WEAK_STRONG, 'Weak and Strong Grip'))


'''WOOD_EXPERIMENTAL_DRILLS = (
    'Wood', (
        (HEEL_TOE, 'Heel and Toe Hits'),
        (THIN_FAT, 'High and Low Face Hits'),
        (WEAK_STRONG, 'Weak and Strong Grip'),),
    'Putting', (
        (WEAK_STRONG, 'Weak and Strong Putt'),
        (TWO_INCH, 'Putts to 2-inch Hole'),
        (THREE_INCH, 'Putts to 3-inch Hole'),),
        )'''
