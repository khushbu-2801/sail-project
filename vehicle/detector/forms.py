from django import forms
from detector.models import *


class uform(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
