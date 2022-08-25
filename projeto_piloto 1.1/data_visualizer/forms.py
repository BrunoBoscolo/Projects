from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

class Filter(forms.Form):
    type = forms.CharField(max_length=100)
    input = forms.CharField(max_length=500)
    range = forms.CharField(max_length=100)