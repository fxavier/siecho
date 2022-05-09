from __future__ import absolute_import, unicode_literals
from celery import shared_task
from openmrs_viamo.services.data_service import AddDataToMiddleware
from core.utils.constants import Constants
from core.utils.province_urls import ProvinceUrl


@shared_task
def print_hello():
    print('Hello')

# ARV DISPENSING ALERTS
@shared_task
def add_arv_dispensing_niassa():
    niassa = ProvinceUrl('Niassa', Constants.niassa_general.value)
    instance = niassa.get_url(Constants.niassa_uuid_reminder.value)
    print(instance)
    AddDataToMiddleware().add_arv_dispensing('Niassa', instance)
    
@shared_task
def add_arv_dispensing_niassa_hpl():
    niassa_hpl = ProvinceUrl('Niassa', Constants.niassa_hpl.value)
    instance = niassa_hpl.get_url(Constants.niassa_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Niassa', instance)
    
@shared_task
def add_arv_dispensing_tete():
    tete = ProvinceUrl('Tete', Constants.tete_general.value)
    instance = tete.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn1():
    tete_csn1 = ProvinceUrl('Tete', Constants.tete_csn1.value)
    instance = tete_csn1.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)

@shared_task
def add_arv_dispensing_tete_csn2():
    tete_csn2 = ProvinceUrl('Tete', Constants.tete_csn2.value)
    instance = tete_csn2.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn3():
    tete_csn3 = ProvinceUrl('Tete', Constants.tete_csn3.value)
    instance = tete_csn3.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn4():
    tete_csn4 = ProvinceUrl('Tete', Constants.tete_csn4.value)
    instance = tete_csn4.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_csn1():
    tete_moatize = ProvinceUrl('Tete', Constants.tete_moatize.value)
    instance = tete_moatize.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_mutarara():
    tete_mutarara = ProvinceUrl('Tete', Constants.tete_mutarara.value)
    instance = tete_mutarara.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_songo():
    tete_songo = ProvinceUrl('Tete', Constants.tete_songo.value)
    instance = tete_songo.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_ulongue():
    tete_ulongue = ProvinceUrl('Tete', Constants.tete_ulongue.value)
    instance = tete_ulongue.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
@shared_task
def add_arv_dispensing_tete_zobue():
    tete_zobue = ProvinceUrl('Tete', Constants.tete_zobue.value)
    instance = tete_zobue.get_url(Constants.tete_uuid_reminder.value)
    AddDataToMiddleware().add_arv_dispensing('Tete', instance)
    
    
# MISSED APPOINTMENT

@shared_task
def add_missed_appointments_niassa():
    niassa = ProvinceUrl('Niassa', Constants.niassa_general.value)
    instance = niassa.get_url(Constants.niassa_uuid_missed_appointment.value)
    print(instance)
    AddDataToMiddleware().add_missed_appointments('Niassa', instance)
    
@shared_task
def add_missed_appointments_niassa_hpl():
    niassa_hpl = ProvinceUrl('Niassa', Constants.niassa_hpl.value)
    instance = niassa_hpl.get_url(Constants.niassa_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Niassa', instance)
    
@shared_task
def add_missed_appointments_tete():
    tete = ProvinceUrl('Tete', Constants.tete_general.value)
    instance = tete.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn1():
    tete_csn1 = ProvinceUrl('Tete', Constants.tete_csn1.value)
    instance = tete_csn1.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)

@shared_task
def add_missed_appointments_tete_csn2():
    tete_csn2 = ProvinceUrl('Tete', Constants.tete_csn2.value)
    instance = tete_csn2.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn3():
    tete_csn3 = ProvinceUrl('Tete', Constants.tete_csn3.value)
    instance = tete_csn3.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn4():
    tete_csn4 = ProvinceUrl('Tete', Constants.tete_csn4.value)
    instance = tete_csn4.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_csn1():
    tete_moatize = ProvinceUrl('Tete', Constants.tete_moatize.value)
    instance = tete_moatize.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_mutarara():
    tete_mutarara = ProvinceUrl('Tete', Constants.tete_mutarara.value)
    instance = tete_mutarara.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_songo():
    tete_songo = ProvinceUrl('Tete', Constants.tete_songo.value)
    instance = tete_songo.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_ulongue():
    tete_ulongue = ProvinceUrl('Tete', Constants.tete_ulongue.value)
    instance = tete_ulongue.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)
    
@shared_task
def add_missed_appointments_tete_zobue():
    tete_zobue = ProvinceUrl('Tete', Constants.tete_zobue.value)
    instance = tete_zobue.get_url(Constants.tete_uuid_missed_appointment.value)
    AddDataToMiddleware().add_missed_appointments('Tete', instance)