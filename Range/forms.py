from django import forms
from .models import Woods_Test, Woods_Technical, Hybrids_Technical, \
    Irons_Technical, Wedges_Technical, Chipping_Technical, \
    Putting_Technical, Woods_Experimental, Wedges_Experimental, \
    Putting_Experimental

class Woods_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Woods_Experimental
        fields = ('date', 'drill', 'detail', 'club', 'shots_hit')

class Woods_Test_Form(forms.ModelForm):

    class Meta:
        model = Woods_Test
        fields = ('date', 'balls_hit', 'center_strike', 'angle_of_attack',
        'club_face_path')


class Woods_Technical_Form(forms.ModelForm):

    class Meta:
        model = Woods_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')



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

class Wedges_Technical_Form(forms.ModelForm):

    class Meta:
        model = Wedges_Technical
        fields = ('date', 'area', 'detail', 'level', 'club', 'shots_hit',
        'shots_success')

class Wedges_Experimental_Form(forms.ModelForm):

    class Meta:
        model = Wedges_Experimental
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
        fields = ('date', 'detail', 'drill', 'shots_hit')
