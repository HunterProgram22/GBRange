from django import forms
from .models import Drill_Base_Model
from .constants import PHASES, WOOD_CLUBS, HYBRID_CLUBS, \
    IRON_CLUBS, WEDGE_CLUBS, CHIPPING_CLUBS, WOOD_EXPERIMENTAL_DRILLS, DRILLS


'''Perhaps use non-model form later to reduce having 36 different form classes'''

'''http://www.ilian.io/django-forms-choicefield-with-dynamic-values/'''

def get_club_choices(club):
    if club == 'Woods':
        return WEDGE_CLUBS
    else:
        return IRON_CLUBS

def get_drill_choices(area):
    if area == 'Experimental':
        return WOOD_EXPERIMENTAL_DRILLS
    else:
        return DRILLS

class Base_Drill_Form(forms.ModelForm):

    def __init__ (self, club, area, *args, **kwargs):
        super(Base_Drill_Form, self).__init__(*args, **kwargs)
        self.fields['drill'] = forms.ChoiceField(choices=get_drill_choices(area))
        self.fields['club'] = forms.ChoiceField(choices=get_club_choices(club))

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

'''class Woods_Experimental_Form(forms.ModelForm):

    def woods():
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Woods'
        self.fields['drill'].choices = WOOD_EXPERIMENTAL_DRILLS
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')'''

class Woods_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Woods'
        self.fields['drill'].choices = WOOD_EXPERIMENTAL_DRILLS
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Woods_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Woods'
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Woods_Calibration_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Calibration'
        self.fields['area'].initial = 'Woods'
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Woods_Test_Form(forms.ModelForm):
    pass


class Hybrids_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Hybrids'
        self.fields['club'].choices = HYBRID_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Hybrids_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Hybrids'
        self.fields['club'].choices = HYBRID_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')


class Irons_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Irons'
        self.fields['club'].choices = IRON_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Irons_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Irons'
        self.fields['club'].choices = IRON_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')


class Wedges_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'DIrect Technical'
        self.fields['area'].initial = 'Wedges'
        self.fields['club'].choices = WEDGE_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')


class Wedges_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Wedges'
        self.fields['club'].choices = WEDGE_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')


class Chipping_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Chipping'
        self.fields['club'].choices = CHIPPING_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Chipping_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Chipping'
        self.fields['club'].choices = CHIPPING_CLUBS

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')



class Putting_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Putting'
        self.fields['club'].initial = 'Putter'

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')

class Putting_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Putting'
        self.fields['club'].initial = 'Putter'

    class Meta:
        model = Drill_Base_Model
        fields = ('__all__')
