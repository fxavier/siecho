# Generated by Django 4.0.3 on 2022-04-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_dataelementvalue_periodperiod_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TxCurrNewPvlsMonth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('element', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxCurrNewPvlsTrim',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('element', models.CharField(max_length=100)),
            ],
        ),
    ]
