from os import name
from django.urls import path 
from core.views import upload_orgunits

app_name = 'core'

urlpatterns = [
    path('', upload_orgunits, name='upload_orgunits')
]