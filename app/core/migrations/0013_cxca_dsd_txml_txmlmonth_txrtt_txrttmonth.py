# Generated by Django 4.0.4 on 2022-05-04 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_dataelement_dataset'),
    ]

    operations = [
        migrations.CreateModel(
            name='CXCA',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DSD',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxML',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxMLMonth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxRTT',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxRTTMonth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
    ]
