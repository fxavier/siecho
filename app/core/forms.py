from django import forms
from core.models import CsvFile, ExcelFile


class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('file_name',)
        
class ExcelForm(forms.ModelForm):
    
    class Meta:
        model = ExcelFile
        fields = ('file_name',)
