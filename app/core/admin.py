from django.contrib import admin
from import_export.admin import ImportExportMixin

from core.models import DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile, Period, \
                        ReportYear, ReportMonth, ReportPeriodType, ReportPeriod, TxCurrNewPvlsTrim, TxCurrNewPvlsMonth, \
                        TxML, TxMLMonth, TxRTT, TxRTTMonth, DSD, CXCA

from openmrs_viamo.models import Visit, MissedAppointment

# classes = [
#     DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile
# ]

# for model in classes:
#     admin.site.register(model)
    
class ReportYearAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'designacao']
    
class TXMLAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class TXMLMonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class TxRTTMonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class TXRTTAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class DSDAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class CXCAAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
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
    list_display = ['dataElement', 'period', 'healthFacility', 'value', 'dataset', 'synced']
    
    
class HealthFacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    ordering = ['province_name']   
    list_display = ['id','code', 'province_name', 'district_name','healthfacility_name']
    
class TxCurrNewPvlsTrimAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class TxCurrNewPvlsMonthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'dataelement', 'code']
    
class VisitAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
             'id', 'province', 'district', 'health_facility','patient_identifier', 'age', 'gender', 'appointment_date',
             'next_appointment_date', 'pregnant'
              ]
    
class MissedAppointmentAdmin(ImportExportMixin, admin.ModelAdmin):
     list_display = [
             'id', 'province', 'district', 'health_facility','patient_identifier', 'age', 'gender',
             'last_appointment_date', 'pregnant'
              ]

admin.site.register(TxML, TXMLAdmin)
admin.site.register(TxMLMonth, TXMLMonthAdmin)
admin.site.register(TxRTT, TXRTTAdmin)
admin.site.register(TxRTTMonth, TxRTTMonthAdmin)
admin.site.register(DSD, DSDAdmin)
admin.site.register(CXCA, CXCAAdmin)
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
admin.site.register(Visit, VisitAdmin)
admin.site.register(MissedAppointment, MissedAppointmentAdmin)