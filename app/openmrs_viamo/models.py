from django.db import models


class Visit(models.Model):
    province = models.CharField(max_length = 150)
    district = models.CharField(max_length = 150, blank=True, null=True)
    health_facility = models.CharField(max_length = 150)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length = 255)
    patient_identifier = models.CharField(max_length =255, null=True, blank=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 150, null=True, blank=True)
    appointment_date = models.DateField()
    next_appointment_date =  models.DateField()
    gender = models.CharField(max_length = 150)
    community = models.CharField(max_length = 500, blank=True, null=True)
    pregnant = models.CharField(max_length =10, default="NAO")
    brestfeeding = models.CharField(max_length =10, default="NAO")
    tb = models.CharField(max_length =10, default="NAO")
    synced = models.BooleanField(default=False)
    
    def __str__(self):
        return self.patient_name

    
class MissedAppointment(models.Model):
    province = models.CharField(max_length = 150)
    district = models.CharField(max_length = 150, blank=True, null=True)
    health_facility = models.CharField(max_length = 150, blank=True, null=True)
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length = 255)
    patient_identifier = models.CharField(max_length =255, null=True, blank=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 150, null=True, blank=True)
    last_appointment_date =  models.DateField(null=True, blank=True)
    gender = models.CharField(max_length = 150, blank=True, null=True)
    community = models.CharField(max_length = 500, blank=True, null=True)
    pregnant = models.CharField(max_length =10, default="NAO", null=True, blank=True)
   # brestfeeding = models.CharField(max_length =10, default="NAO")
   # tb = models.CharField(max_length =10, default="NAO")
    drug_pickup_missed_days = models.IntegerField(default=0, null=True, blank=True)
    visit_missed_days = models.IntegerField(default=0, null=True, blank=True)
    synced = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.patient_name




