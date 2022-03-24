from django.db import models


class ExcelFile(models.Model):
    file_name = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'
    
class CsvFile(models.Model):
    file_name = models.FileField()
    date_created = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'


class Province(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class District(models.Model):
    """Model definition for District."""

    # TODO: Define fields here
    name = models.CharField(max_length=100)
    province = models.ForeignKey('Province', on_delete=models.CASCADE)
   
    def __str__(self):
        """Unicode representation of District."""
        return self.name

class HealthFacility(models.Model):
    """Model definition for HealthFacility."""
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    # openmrs_name = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for HealthFacility."""

        verbose_name = 'Health Facility'
        verbose_name_plural = 'Health Facilities'

    def __str__(self):
        """Unicode representation of HealthFacility."""
        return self.name

    
class DataSet(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.name


class DataElement(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    openmrs = models.CharField(max_length=100, null=True, blank=True)
    categoryOptionCombo = models.CharField(max_length=200, null=True, blank=True)
    attributeOptionCombo = models.CharField(max_length=200, null=True, blank=True)
    dataSet = models.ForeignKey(DataSet, on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.name

class DataElementValue(models.Model):
    period = models.CharField(max_length=100)
    value = models.IntegerField(null=True, blank=True) 
    healthFacility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    dataElement = models.ForeignKey('DataElement', on_delete=models.CASCADE)
    synced = models.BooleanField(default=False)
    
    def __str__(self):
        return self.dataElement.name
