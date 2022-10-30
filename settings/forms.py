from django import forms
from .models import Api


class ApiForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = ['api']
