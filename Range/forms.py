from django import forms
from .models import Drill_Base_Model
from .constants import PHASES, WOOD_CLUBS, HYBRID_CLUBS, \
    IRON_CLUBS, WEDGE_CLUBS, CHIPPING_CLUBS


class Woods_Experimental_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Experimental'
        self.fields['area'].initial = 'Woods'
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        exclude = ['shots_success', 'level']

class Woods_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Woods'
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        exclude = ['drill']

class Woods_Calibration_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Calibration'
        self.fields['area'].initial = 'Woods'
        self.fields['club'].choices = WOOD_CLUBS

    class Meta:
        model = Drill_Base_Model
        exclude = ['shots_success', 'level']

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
        exclude = ['shots_success', 'level']

class Hybrids_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Hybrids'
        self.fields['club'].choices = HYBRID_CLUBS

    class Meta:
        model = Drill_Base_Model
        exclude = ['drill']


class Irons_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'
        self.fields['area'].initial = 'Irons'
        self.fields['club'].choices = IRON_CLUBS

    class Meta:
        model = Drill_Base_Model
        exclude = ['drill']

class Irons_Experimental_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'Experimental'
            self.fields['area'].initial = 'Irons'
            self.fields['club'].choices = IRON_CLUBS

        class Meta:
            model = Drill_Base_Model
            exclude = ['shots_success', 'level']


class Wedges_Technical_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'DIrect Technical'
            self.fields['area'].initial = 'Wedges'
            self.fields['club'].choices = WEDGE_CLUBS

        class Meta:
            model = Drill_Base_Model
            exclude = ['drill']


class Wedges_Experimental_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'Experimental'
            self.fields['area'].initial = 'Wedges'
            self.fields['club'].choices = WEDGE_CLUBS

        class Meta:
            model = Drill_Base_Model
            exclude = ['shots_success', 'level']


class Chipping_Experimental_Form(forms.ModelForm):

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['phase'].initial = 'Experimental'
                self.fields['area'].initial = 'Chipping'
                self.fields['club'].choices = CHIPPING_CLUBS

            class Meta:
                model = Drill_Base_Model
                exclude = ['shots_success', 'level']

class Chipping_Technical_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'Direct Technical'
            self.fields['area'].initial = 'Chipping'
            self.fields['club'].choices = CHIPPING_CLUBS

        class Meta:
            model = Drill_Base_Model
            exclude = ['drill']



class Putting_Technical_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'Direct Technical'
            self.fields['area'].initial = 'Putting'
            self.fields['club'].initial = 'Putter'

        class Meta:
            model = Drill_Base_Model
            exclude = ['drill']

class Putting_Experimental_Form(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['phase'].initial = 'Experimental'
            self.fields['area'].initial = 'Putting'
            self.fields['club'].initial = 'Putter'

        class Meta:
            model = Drill_Base_Model
            exclude = ['shots_success', 'level']
