from django import forms
from .models import Woods_Test, Woods_Technical

class Woods_Test_Form(forms.ModelForm):

    class Meta:
        model = Woods_Test
        fields = ('date', 'balls_hit', 'center_strike', 'angle_of_attack',
        'club_face_path')

class Woods_Technical_Form(forms.ModelForm):

    class Meta:
        model = Woods_Technical
        fields = ('date', 'area', 'detail', 'level', 'shots_hit',
        'shots_success')
