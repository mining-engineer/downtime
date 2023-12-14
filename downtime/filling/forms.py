from django.forms import ModelForm
from django import forms

from .models import Downtime


class FillingForm(ModelForm):
    class Meta:
        model = Downtime
        fields = "__all__"
        widgets = {
            'downtime': forms.DateInput(attrs={'type': 'date'})
        } 
