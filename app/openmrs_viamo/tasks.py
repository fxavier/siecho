from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs_viamo.services.data_service import AddDataToMiddleware, PostData
from core.utils.province_urls import ProvinceUrl
from core.utils.constants import Constants
from openmrs_viamo.models import Visit, MissedAppointment
from si_stock.models import Resumo
from si_stock.data_service import get_resumo_data

UUID_REMINDER = Constants.uuid_reminder.value
UUID_MISSED_APPOINTMENT = Constants.uuid_missed_appointment.value

@shared_task
def insert_resumo():
    resumo =  Resumo.objects.all()
    if resumo:
        resumo.delete()
    get_resumo_data()

# ARV DISPENSING ALERTS
@shared_task
def add_arv_dispensing_niassa():
    niassa = ProvinceUrl('Niassa', Constants.niassa_general.value)
    instance = niassa.get_url(UUID_REMINDER)
    print(instance)
    AddDataToMiddleware().add_arv_dispensing('Niassa', instance)
    
@shared_task
def add_arv_dispensing_niassa_hpl():
    niassa_hpl = ProvinceUrl('Niassa', Constants.niassa_hpl.value)
    instance = niassa_hpl.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Niassa', instance)
    
@shared_task
def add_arv_dispensing_tete():
    tete = ProvinceUrl('Tete', Constants.tete_general.value)
    instance = tete.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn1():
    tete_csn1 = ProvinceUrl('Tete', Constants.tete_csn1.value)
    instance = tete_csn1.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)

@shared_task
def add_arv_dispensing_tete_csn2():
    tete_csn2 = ProvinceUrl('Tete', Constants.tete_csn2.value)
    instance = tete_csn2.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn3():
    tete_csn3 = ProvinceUrl('Tete', Constants.tete_csn3.value)
    instance = tete_csn3.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn4():
    tete_csn4 = ProvinceUrl('Tete', Constants.tete_csn4.value)
    instance = tete_csn4.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_moatize():
    tete_moatize = ProvinceUrl('Tete', Constants.tete_moatize.value)
    instance = tete_moatize.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_mutarara():
    tete_mutarara = ProvinceUrl('Tete', Constants.tete_mutarara.value)
    instance = tete_mutarara.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_songo():
    tete_songo = ProvinceUrl('Tete', Constants.tete_songo.value)
    instance = tete_songo.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_ulongue():
    tete_ulongue = ProvinceUrl('Tete', Constants.tete_ulongue.value)
    instance = tete_ulongue.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_zobue():
    tete_zobue = ProvinceUrl('Tete', Constants.tete_zobue.value)
    instance = tete_zobue.get_url(UUID_REMINDER)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
    
# MISSED APPOINTMENT

@shared_task
def add_missed_appointments_niassa():
    niassa = ProvinceUrl('Niassa', Constants.niassa_general.value)
    instance = niassa.get_url(UUID_MISSED_APPOINTMENT)
    print(instance)
    AddDataToMiddleware().add_missed_appointments('Niassa', instance)
    
@shared_task
def add_missed_appointments_niassa_hpl():
    niassa_hpl = ProvinceUrl('Niassa', Constants.niassa_hpl.value)
    instance = niassa_hpl.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Niassa', instance)
    
@shared_task
def add_missed_appointments_tete():
    tete = ProvinceUrl('Tete', Constants.tete_general.value)
    instance = tete.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn1():
    tete_csn1 = ProvinceUrl('Tete', Constants.tete_csn1.value)
    instance = tete_csn1.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)

@shared_task
def add_missed_appointments_tete_csn2():
    tete_csn2 = ProvinceUrl('Tete', Constants.tete_csn2.value)
    instance = tete_csn2.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn3():
    tete_csn3 = ProvinceUrl('Tete', Constants.tete_csn3.value)
    instance = tete_csn3.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn4():
    tete_csn4 = ProvinceUrl('Tete', Constants.tete_csn4.value)
    instance = tete_csn4.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_moatize():
    tete_moatize = ProvinceUrl('Tete', Constants.tete_moatize.value)
    instance = tete_moatize.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_mutarara():
    tete_mutarara = ProvinceUrl('Tete', Constants.tete_mutarara.value)
    instance = tete_mutarara.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_songo():
    tete_songo = ProvinceUrl('Tete', Constants.tete_songo.value)
    instance = tete_songo.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_ulongue():
    tete_ulongue = ProvinceUrl('Tete', Constants.tete_ulongue.value)
    instance = tete_ulongue.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_zobue():
    tete_zobue = ProvinceUrl('Tete', Constants.tete_zobue.value)
    instance = tete_zobue.get_url(UUID_MISSED_APPOINTMENT)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def post_sms_reminder():
    PostData.post_sms_reminder()
    
@shared_task
def post_missed_appointment():
    PostData.post_missed_appointment()
    

# Deleting data
    
@shared_task   
def delete_visits():
    Visit.objects.all().delete()

@shared_task  
def delete_missed_appointments():
    MissedAppointment.objects.all().delete()
    
@shared_task 
def update_visits():
    visit = Visit.objects.filter(synced=False)
    for data in visit:
        data.synced = True
        data.save()
    
@shared_task 
def update_missed_appointments():
    missed_appointment = MissedAppointment.objects.filter(synced=False)
    for data in missed_appointment:
        data.synced = True
        data.save()
    
    