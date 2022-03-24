from django.shortcuts import render
from core.forms import CsvForm
from core.models import CsvFile, Province, District, HealthFacility

import csv 

def upload_orgunits(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        csv_file = CsvFile.objects.get(activated=False)
        csv_file.activated = True
        csv_file.save()
        
    # with open(csv_file.file_name.path, 'r') as file:
    #     data = csv.reader(file)
    #     next(data)
    #     for row in data:
    #         province, created = Province.objects.get_or_create(name=row[0])
    #         district, created = District.objects.get_or_create(name=row[1], province=province)
    #         healthfacility, created = HealthFacility.objects.get_or_create(name=row[2], district=district)
            
    #         province.save()
    #         district.save()
    #         healthfacility.save()
    
    
    return render(request, 'app/upload.html', {'form': form})
            


