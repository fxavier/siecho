# Generated by Django 4.0.3 on 2022-04-01 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthfacility',
            old_name='openmrs_code',
            new_name='id',
        ),
    ]
