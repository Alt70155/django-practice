from django import forms
from .models import Request

class RequestCreateForm(forms.ModelForm):

    class Meta:
        model = Request
        exclude = ('user',)
        