# Generated by Django 4.0.3 on 2022-04-01 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_period_id_alter_period_openmrs_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='period',
            old_name='openmrs_designation',
            new_name='id',
        ),
    ]