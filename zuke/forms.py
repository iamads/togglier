__author__ = 'ads'
from django import forms
from zuke.models import Devices


class DevicesForm(forms.ModelForm):
    Device_1 = forms.BooleanField()
    Device_2 = forms.BooleanField()
    Device_3 = forms.BooleanField()
    Device_4 = forms.BooleanField()

    class Meta:
        models = Devices
