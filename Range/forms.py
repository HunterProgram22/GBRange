from django import forms
from .models import Pass_Fail_Drill

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

class WoodsDrillForm(forms.ModelForm):

    class Meta:
        model = Pass_Fail_Drill
        fields = ['name', 'date', 'practice_area', 'club',
                    'balls_hit', 'balls_succesful']
        widgets = {
                    'practice_area': forms.RadioSelect(choices=PRACTICE_AREAS),
                    }
