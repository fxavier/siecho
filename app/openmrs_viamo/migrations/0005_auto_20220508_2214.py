# Generated by Django 3.2.13 on 2022-05-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openmrs_viamo', '0004_remove_missedappointment_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missedappointment',
            name='gender',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='missedappointment',
            name='health_facility',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
