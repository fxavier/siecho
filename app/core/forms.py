from django import forms
from core.models import CsvFile


class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('file_name',)
