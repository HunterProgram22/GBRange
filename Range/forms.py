from django import forms
from .models import Drill_Base_Model
from .constants import PHASES


class Woods_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Drill_Base_Model
        fields = ('date', 'phase', 'drill', 'detail', 'club', 'shots_hit')

class Woods_Test_Form(forms.ModelForm):
    pass

class Woods_Technical_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phase'].initial = 'Direct Technical'

    class Meta:
        model = Drill_Base_Model
        fields = ('date', 'area', 'phase', 'detail', 'level', 'club', 'drill',
                  'shots_hit', 'shots_success')

'''        
class Woods_Calibration_Form(forms.ModelForm):
    
    class Meta:
        model = Woods_Calibration
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Hybrids_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Hybrids_Experimental
        fields = ('date', 'drill', 'detail', 'club', 'shots_hit')

class Hybrids_Technical_Form(forms.ModelForm):

    class Meta:
        model = Hybrids_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Irons_Technical_Form(forms.ModelForm):

    class Meta:
        model = Irons_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Irons_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Irons_Experimental
        fields = ('date', 'drill', 'detail', 'club', 'shots_hit')

class Wedges_Technical_Form(forms.ModelForm):

    class Meta:
        model = Wedges_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Wedges_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Wedges_Experimental
        fields = ('date', 'drill', 'detail', 'club', 'shots_hit')

class Chipping_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Chipping_Experimental
        fields = ('date', 'drill', 'detail', 'club', 'shots_hit')

class Chipping_Technical_Form(forms.ModelForm):

    class Meta:
        model = Chipping_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Putting_Technical_Form(forms.ModelForm):

    class Meta:
        model = Putting_Technical
        fields = ('date', 'area', 'detail', 'level', 'shots_hit',
        'shots_success')

class Putting_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Putting_Experimental
        fields = ('date', 'detail', 'drill', 'shots_hit')'''
