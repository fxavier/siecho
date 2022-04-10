from django.contrib import admin
from import_export.admin import ImportExportMixin

from core.models import DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile, Period, \
                        ReportYear, ReportMonth, ReportPeriodType, ReportPeriod, TxCurrNewPvlsTrim, TxCurrNewPvlsMonth

# classes = [
#     DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile
# ]

# for model in classes:
#     admin.site.register(model)
    
class ReportYearAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'designacao']
    
class ReportMonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'month', 'code', 'reportperiodtype']
    
class ReportPeriodTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'designation']
    
class ReportPeriodAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'reportyear', 'reportmonth', 'dhis_format']
class PeriodAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dhis_designation', 'period_type']
    list_filter = ('period_type', 'dhis_designation')
    
class DataElementAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name', 'categoryOptionCombo', 'attributeOptionCombo', 'dataSet']
    
class DataSetAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name']
    
class DataElementValueAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ['period']
    list_display = ['dataElement', 'period', 'healthFacility', 'value', 'synced']
    
    
class HealthFacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ['province_name']   
    list_display = ['id','code', 'province_name', 'district_name','healthfacility_name']
    
class TxCurrNewPvlsTrimAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'element']
    
class TxCurrNewPvlsMonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'element']

    
admin.site.register(Period, PeriodAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataElementValue, DataElementValueAdmin)
admin.site.register(ExcelFile)
admin.site.register(CsvFile)
admin.site.register(ReportPeriodType, ReportPeriodTypeAdmin)
admin.site.register(ReportYear, ReportYearAdmin)
admin.site.register(ReportMonth, ReportMonthAdmin)
admin.site.register(ReportPeriod, ReportPeriodAdmin)
admin.site.register(TxCurrNewPvlsTrim, TxCurrNewPvlsTrimAdmin)
admin.site.register(TxCurrNewPvlsMonth, TxCurrNewPvlsMonthAdmin)