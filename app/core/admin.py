from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin

from core.models import DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile, Period, \
                        ReportYear, ReportMonth, ReportPeriodType, ReportPeriod, TxCurrNewPvlsTrim, TxCurrNewPvlsMonth, \
                        TxML, TxMLMonth, TxRTT, TxRTTMonth, DSD, CXCA

from openmrs_viamo.models import Visit, MissedAppointment

from assistencia_tecnica.models import Provincia, Distrito, UnidadeSanitaria, Sector, Area, Indicador, FichaAssistenciaTecnica
from user.models import User
from si_stock import models

# classes = [
#     DataSet, Province, District, HealthFacility, DataElement, DataElementValue, ExcelFile, CsvFile
# ]

# for model in classes:
#     admin.site.register(model)


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    
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
             'next_appointment_date', 'synced'
              ]
    
class MissedAppointmentAdmin(ImportExportMixin, admin.ModelAdmin):
     list_display = [
             'id', 'province', 'district', 'health_facility','patient_identifier', 'age', 'gender',
             'last_appointment_date', 'synced'
              ]
     
class ProvinciaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome']
    
class DistritoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome', 'provincia']
    

class UnidadeSanitariaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome', 'distrito']
    
class SectorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id','nome']
    
class AreaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome', 'sector']
    
class IndicadorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome', 'area'] 
    
class FichaAssistenciaTecnicaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome_responsavel', 'nome_provedor', 'problemas_identificados', 'tipo_problema', 'atcividades_realizar_resolver_problema']
    
    
class ProvinciaAdminStock(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome']

class SectorAdminStock(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'provincia', 'nome']
    list_filter = ('nome', 'provincia',)
    
class InstrumentoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'provincia', 'sector', 'nome', 'stock', 'ano', 'quantidade_necessaria']
    list_filter = ('provincia', 'sector', 'nome',)
    
class NecessidadeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'provincia', 'sector', 'instrumento', 'ano', 'quantidade']
    list_filter = ('provincia', 'sector',)
    
class EntradaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'data_entrada', 'fornecedor', 'quantidade', 'provincia','instrumento']
    list_filter = ('provincia',)
    
class LevantamentoDepositoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'data_levantamento', 'provincia', 'instrumento', 'quantidade']
    
class RequisicaoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'data_requisicao', 'provincia', 'instrumento', 'quantidade', 'status_requisicao']
    
class AprovacaoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'requisicao', 'tipo_aprovacao', 'comentario']
    
class ResumoAdmin(admin.ModelAdmin):
    list_display = ['provincia', 'sector', 'instrumento', 'data_entrada', 'quantidade', 'stock', 'necessidade', 'data_requisicao', 'quantidade_requisicao', 'status_requisicao']
    list_filter = ('provincia', 'sector',)

admin.site.register(User, UserAdmin)
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
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(UnidadeSanitaria, UnidadeSanitariaAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(FichaAssistenciaTecnica, FichaAssistenciaTecnicaAdmin)
admin.site.register(models.Provincia, ProvinciaAdminStock)
admin.site.register(models.Sector, SectorAdminStock)
admin.site.register(models.Instrumento, InstrumentoAdmin)
admin.site.register(models.Necessidade, NecessidadeAdmin)
admin.site.register(models.Entrada, EntradaAdmin)
admin.site.register(models.Requisicao, RequisicaoAdmin)
admin.site.register(models.Aprovacao, AprovacaoAdmin)
admin.site.register(models.Resumo, ResumoAdmin)