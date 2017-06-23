from django import forms
from .models import Drill_Base_Model
from .constants import PHASES, WOOD_CLUBS, HYBRID_CLUBS, \
    IRON_CLUBS, WEDGE_CLUBS, CHIPPING_CLUBS, PUTTING_CLUB, \
    WOOD_EXPERIMENTAL_DRILLS, DRILLS


def get_initial_area(club):
    if club == 'Woods':
        return 'Woods'
    elif club == 'Hybrids':
        return 'Hybrids'
    elif club == 'Irons':
        return 'Irons'
    elif club == 'Wedges':
        return 'Wedges'
    elif club == 'Chipping':
        return 'Chipping'
    else:
        return 'Putting'

def get_initial_phase(area):
    if area == 'Test':
        return 'Test'
    elif area == 'Technical':
        return 'Direct Technical'
    elif area == 'Experimental':
        return 'Experimental'
    elif area == 'Calibration':
        return 'Calibration'
    elif area == 'Performance':
        return 'Performance'
    else:
        return 'Games'

def get_club_choices(club):
    if club == 'Woods':
        return WOOD_CLUBS
    elif club == 'Hybrids':
        return HYBRID_CLUBS
    elif club == 'Irons':
        return IRON_CLUBS
    elif club == 'Wedges':
        return WEDGE_CLUBS
    elif club == 'Chipping':
        return CHIPPING_CLUBS
    else:
        return PUTTING_CLUB

def get_drill_choices(area):
    if area == 'Test':
        return DRILLS
    elif area == 'Technical':
        return DRILLS
    elif area == 'Experimental':
        return DRILLS
    elif area == 'Calibration':
        return DRILLS
    elif area == 'Performance':
        return DRILLS
    else:
        return DRILLS

'''See the following link for information on initiating choices for form fields
http://www.ilian.io/django-forms-choicefield-with-dynamic-values/'''

class Base_Drill_Form_GET(forms.ModelForm):

    def __init__ (self, club, area, *args, **kwargs):
        super(Base_Drill_Form_GET, self).__init__(*args, **kwargs)
        self.fields['area'] = forms.CharField(initial=get_initial_area(club))
        self.fields['phase'] = forms.CharField(initial=get_initial_phase(area))
        self.fields['drill'] = forms.ChoiceField(choices=get_drill_choices(area))
        self.fields['club'] = forms.ChoiceField(choices=get_club_choices(club))

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')


class Base_Drill_Form_POST(forms.ModelForm):

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')
