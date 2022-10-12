from django import forms
from .models import API


class ApiForm(forms.ModelForm):
    class Meta:
        model = API
        fields = ['api']
