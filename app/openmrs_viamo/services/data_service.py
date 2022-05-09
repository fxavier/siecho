import requests
from  django.db.models import Q
from dataclasses import dataclass
from openmrs_viamo.models import Visit, MissedAppointment
from datetime import datetime, timedelta, date
from core.utils.constants import Constants
from core.utils.data_conversion import DataConversion

@dataclass
class FetchOpenMRSData:
    
    def get_arv_dispensing(self, instance):
        start_date = date.today()  + timedelta(days=4)
        end_date = start_date + timedelta(days=4)
        params = {
            'startDate': str(start_date),
            'endDate': str(end_date)
            }
        try:
            response = requests.get(instance, params=params, auth=Constants.openmrs_auth.value)
            data_list = response.json()['rows']
            return data_list
        except requests.exceptions.RequestException as err:
            print(err)
            
            
    def get_misssed_appointment(self, instance):
        end_date = date.today() - timedelta(days=2)
        params = {
            'endDate': str(end_date)
            }
        try:
            response = requests.get(instance, params=params, auth=Constants.openmrs_auth.value)
            data_list = response.json()['rows']
            return data_list
        except requests.exceptions.RequestException as err:
            print(err)        
            
            
@dataclass     
class AddDataToMiddleware:
    
    @staticmethod
    def add_arv_dispensing(province, instance):
        data_list = FetchOpenMRSData().get_arv_dispensing(instance)
        
        if data_list is not None:
            for data in data_list:
                visit, created = Visit.objects.get_or_create(
                province=province,
                district=data['Distrito'],
                health_facility=data['us'],
                patient_id=data['patient_id'],
                patient_name=data['NomeCompleto'],
                patient_identifier=data['NID'], 
                age=data['age'],
                phone_number=data['phone_number'],
                appointment_date=datetime.fromtimestamp(data['dispensing_date'] / 1e3),
                next_appointment_date=datetime.fromtimestamp(data['next_dispensing_date'] / 1e3),
                gender=data['gender'],
                community=data['Bairro'],
                pregnant=data['pregnant'],
                brestfeeding=data['brestfeeding'],
                tb=data['tb']
               )
                visit.save()
    
    @staticmethod
    def add_missed_appointments(province, instance):
        data_list = FetchOpenMRSData().get_misssed_appointment(instance)
        if data_list is not None:
            for data in data_list:
                missed_appointment, created = MissedAppointment.objects.get_or_create(
                province=province,
                district=data['Distrito'],
                health_facility=data['us'],
                patient_id=data['patient_id'],
                patient_name=data['nome'],
                patient_identifier=data['NID'], 
                age=data['idade_actual'],
                phone_number=data['Telefone'],
                last_appointment_date=DataConversion.convert_int_date(data['ultimo_lev']),  #datetime.fromtimestamp(data['ultimo_lev'] / 1e3),
                gender=data['gender'],
                community=data['Bairro'],
                pregnant=data['p_gestante'],
                drug_pickup_missed_days=data['dias_falta_lev'],
                visit_missed_days=data['dias_falta_seg']
            )
                
            missed_appointment.save()
            
@dataclass          
class PostData:
    api_url = Constants.viamo_api_url.value
    api_key = Constants.viamo_api_key.value
    
    @classmethod
    def post_sms_reminder(cls):
        payload_list = []
        visit = Visit.objects.exclude(phone_number=None).filter(synced=False)
        for v in visit:
            phone = v.phone_number.strip()
            payload = {
                "api_key": cls.api_key,
                "phone": phone[:9],
                "receive_voice": "1",
                "receive_sms": "1",
                "preferred_channel": "1",
                "groups": "463089",
                "active": "1",
            }
                        
            data_values = {
             "patient_identifier": v.patient_identifier,
             "appointment_date": '{:%Y-%m-%d}'.format(v.next_appointment_date),
             "actual_visit_date": '{:%Y-%m-%d}'.format(v.appointment_date),
             "gender": v.gender,
             "pregnant": v.pregnant,
             "age": v.age,
             "district": v.district,
             "province": v.province,
             "health_facility": v.health_facility
            }
        
            payload['property'] = data_values
            payload_list.append(payload)
            
        records = 0
        try:
            for data in payload_list:
                records += 1
                response = requests.post(cls.api_url, json=data)
                print(f'Sending {records} of {len(payload_list)} Records')
                print(response.raise_for_status)

        except requests.exceptions.RequestException as err:
            print(err)
            
    @classmethod       
    def post_missed_appointment(cls):
        payload_list = []
        missed_appointment = MissedAppointment.objects.exclude(phone_number=None).filter(synced=False, drug_pickup_missed_days__gt=0, visit_missed_days__gt=0)
        for m in missed_appointment:
            phone = m.phone_number.strip()
            payload = {
                "api_key": cls.api_key,
                "phone": phone[:9],
                "receive_voice": "1",
                "receive_sms": "1",
                "preferred_channel": "1",
                "groups": "463089",
                "active": "1",
            }
                        
            data_values = {
             "patient_identifier": m.patient_identifier,
             "last_appointment_date": '{:%Y-%m-%d}'.format(m.last_appointment_date),
             "actual_visit_date": '{:%Y-%m-%d}'.format(m.appointment_date),
             "gender": m.gender,
             "pregnant": m.pregnant,
             "age": m.age,
             "district": m.district,
             "province": m.province,
             "health_facility": m.health_facility
            }
        
            payload['property'] = data_values
            payload_list.append(payload)
            
        records = 0
        try:
            for data in payload_list:
                records += 1
                response = requests.post(cls.api_url, json=data)
                print(f'Sending {records} of {len(payload_list)} Records')
                print(response.raise_for_status)

        except requests.exceptions.RequestException as err:
            print(err)
            