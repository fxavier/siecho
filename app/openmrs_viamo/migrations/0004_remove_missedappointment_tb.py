# Generated by Django 3.2.13 on 2022-05-08 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openmrs_viamo', '0003_remove_missedappointment_brestfeeding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missedappointment',
            name='tb',
        ),
    ]
