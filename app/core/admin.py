from django.contrib import admin

from core.models import DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile

classes = [
    DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile
]

for model in classes:
    admin.site.register(model)