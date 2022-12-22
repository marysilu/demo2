from django import forms
from .models import Plants


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['pname', 'rate']
