# Generated by Django 4.0.3 on 2022-04-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_dataelementvalue_periodperiod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataelementvalue',
            name='periodperiod',
        ),
        migrations.AddField(
            model_name='dataelementvalue',
            name='period',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.period'),
            preserve_default=False,
        ),
    ]
