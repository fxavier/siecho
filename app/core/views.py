from django.http import HttpResponse
from django.shortcuts import render
from core.forms import CsvForm, ExcelForm
from core.models import CsvFile, ExcelFile, Province, District, HealthFacility, Period, DataElementValue, DataElement,\
    TxCurrNewPvlsTrim, TxCurrNewPvlsMonth, DataSet

import csv
import os
import openpyxl
from dhis2 import Api
import requests
import datetime
from core.models import TxCurrCounter

from rest_framework import viewsets, mixins, generics
from core.serializers import TxCurrCounterSerializer


path = '../vol/web/media/'
classes = [TxCurrNewPvlsTrim, TxCurrNewPvlsMonth]
api = Api('https://dhis2sand.echomoz.org', 'xnhagumbe', 'Go$btgo1')
data = {}
dataList = []
payload = {}


def upload_orgunits(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        csv_file = CsvFile.objects.get(activated=False)
        csv_file.activated = True
        csv_file.save()

        print(csv_file.file_name)
        Province.objects.all().delete()
        District.objects.all().delete()
        HealthFacility.objects.all().delete()
        path = '../vol/web/media/'
        abspath = os.path.join(path, str(csv_file.file_name))
        print(abspath)
        with open(abspath, 'r') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                province, created = Province.objects.get_or_create(name=row[0])
                district, created = District.objects.get_or_create(
                    name=row[1], province=province)
                healthfacility, created = HealthFacility.objects.get_or_create(
                    code=row[3], name=row[2], openmrs_code=row[4], district=district)

                province.save()
                district.save()
                healthfacility.save()
    return render(request, 'app/upload.html', {'form': form})


def upload_tx_curr_new_pvls(request):
    form = ExcelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExcelForm()
        excel_file = ExcelFile.objects.get(activated=False)
        excel_file.activated = True
        excel_file.save()

        workbook = openpyxl.load_workbook(path + str(excel_file.file_name))
        worksheet = workbook['TX NEW CURR AND PVLS']
        period = Period.objects.get(pk=worksheet["B8"].value)
        if period.period_type == 'Q':
            obj = classes[0]
        elif period.period_type == 'M':
            obj = classes[1]
        for rows in worksheet.iter_rows(min_row=8):
            keycode = rows[0].value
            if not keycode:
                keycode = '99999'
            healthFacility = HealthFacility.objects.get(pk=keycode)
            dataElement = obj.objects.get(pk=5)
            for j in range(5, 244):
                velement = obj.objects.get(pk=j)
                if velement.code == 'code':
                    continue
                dataElement = DataElement.objects.get(pk=velement.code)
                #print(dataElement.name, dataElement.id)
                dataset = DataSet.objects.get(pk=dataElement.dataSet.id)
                dataElementValue = DataElementValue.objects.create(
                    value=int(rows[j].value),
                    healthFacility=healthFacility,
                    dataElement=dataElement,
                    period=period,
                    dataset=dataset
                )
                dataElementValue.save()

    return render(request, 'app/tx_curr_new_pvls.html', {'form': form})


def update_sync_status():
    period = Period.objects.get(pk='21/Dec/2021 - 20/Jan/2022')

    dataElementValue = DataElementValue.objects.filter(
        synced=False, period=period)

    for dt in dataElementValue:
        dt.synced = True
        dt.save()


def post_tx_curr_new_pvls(request):
    period = Period.objects.get(pk='21/Dec/2021 - 20/Jan/2022')
    dataSet = DataSet.objects.get(name='ECHO MOZ | TX_CURR')

    dataElementValue = DataElementValue.objects.filter(
        synced=False, period=period, dataset=dataSet)

    for dt in dataElementValue:
        data["dataElement"] = str(dt.dataElement.id)
        data["period"] = str(period.dhis_designation)
        data["orgUnit"] = str(dt.healthFacility.code)
        data["value"] = str(dt.value)

        dataList.append(data.copy())

    payload["dataValues"] = dataList

    try:
        response = api.post('dataValueSets', json=payload)
        print(response.json()['description'])
        print(response.json()['importCount'])
        update_sync_status()
    except requests.exceptions.RequestException as err:
        print(err)

    # for dt in dataElementValue:
    #     data['dataSet'] = dt.dataElement.dataSet.id
    #     for dt in dataElementValue:
    #         data['period'] = dt.period.dhis_designation
    #         data['orgUnit'] = dt.healthFacility.code
    #         dataElements = {
    #             'dataElement': dt.dataElement.id,
    #             'value': dt.value

    #         }
    #         dataList.append(dataElements)
    #     data['dataValues'] = dataList
    #     try:
    #         response = api.post('dataValueSets', json=data)
    #         print(response.status.code)
    #         print(response.json()['importCount'])
    #         print(data)
    #     except requests.exceptions.RequestException as err:
    #         print(err)
    # now = datetime.datetime.now()
    # html = "<html><body>payload %s.</body></html>" % now

    return HttpResponse("Done")


class TxCurrCounterViewset(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = TxCurrCounter.objects.all()
    serializer_class = TxCurrCounterSerializer
