from django.db import models


PERIOD_TYPE = (
    ('M', 'Mensal'),
    ('Q', 'Trimestral'),
    ('S', 'Semestral'),
    ('A', 'Anual')
)


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
    code = models.CharField(max_length=255)
    province_name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)
    healthfacility_name = models.CharField(max_length=255)
    # district = models.ForeignKey('District', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for HealthFacility."""

        verbose_name = 'Health Facility'
        verbose_name_plural = 'Health Facilities'

    def __str__(self):
        """Unicode representation of HealthFacility."""
        return self.healthfacility_name


class DataSet(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class DataElement(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
   # openmrs = models.CharField(max_length=100, null=True, blank=True)
    categoryOptionCombo = models.CharField(
        max_length=200, null=True, blank=True)
    attributeOptionCombo = models.CharField(
        max_length=200, null=True, blank=True)
    dataSet = models.ForeignKey(
        DataSet, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class DataElementValue(models.Model):
    value = models.IntegerField(null=True, blank=True)
    healthFacility = models.ForeignKey(
        HealthFacility, on_delete=models.CASCADE)
    dataElement = models.ForeignKey('DataElement', on_delete=models.CASCADE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE)
    synced = models.BooleanField(default=False)
    dataset = models.ForeignKey('DataSet', on_delete=models.CASCADE)

    def __str__(self):
        return self.dataElement.name


class Period(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    dhis_designation = models.CharField(max_length=100)
    period_type = models.CharField(max_length=2, choices=PERIOD_TYPE)

    def __str__(self):
        return self.id


class ReportYear(models.Model):
    designacao = models.CharField(max_length=10)

    def __str__(self):
        return self.designacao


class ReportPeriodType(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class ReportMonth(models.Model):
    month = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    reportperiodtype = models.ForeignKey(
        ReportPeriodType, on_delete=models.CASCADE)

    def __str__(self):
        return self.month


class ReportPeriod(models.Model):
    reportyear = models.ForeignKey(ReportYear, on_delete=models.CASCADE)
    reportmonth = models.ForeignKey(ReportMonth, on_delete=models.CASCADE)
    dhis_format = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.dhis_format)


class TxCurrNewPvlsTrim(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxCurrNewPvlsMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxML(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxMLMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxRTT(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxRTTMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class DSD(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class CXCA(models.Model):
    id = models.IntegerField(primary_key=True)
    dataelement = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dataelement)


class TxCurrCounter(models.Model):
    date = models.DateField()
    hour = models.PositiveIntegerField()
    value = models.IntegerField()

    def increment_value(self):
        self.value += 7
        self.save()

    def __str__(self):
        return str(f'{self.value} - {self.date} - {self.hour}')
