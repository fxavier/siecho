# Generated by Django 3.2.14 on 2022-08-02 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CXCA',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataElement',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('categoryOptionCombo', models.CharField(blank=True, max_length=200, null=True)),
                ('attributeOptionCombo', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
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
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('province_name', models.CharField(max_length=255)),
                ('district_name', models.CharField(max_length=255)),
                ('healthfacility_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Health Facility',
                'verbose_name_plural': 'Health Facilities',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dhis_designation', models.CharField(max_length=100)),
                ('period_type', models.CharField(choices=[('M', 'Mensal'), ('Q', 'Trimestral'), ('S', 'Semestral'), ('A', 'Anual')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReportMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReportPeriodType',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReportYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designacao', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TxCurrNewPvlsMonth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dataelement', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TxCurrNewPvlsTrim',
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
        migrations.CreateModel(
            name='ReportPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dhis_format', models.CharField(blank=True, max_length=100, null=True)),
                ('reportmonth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reportmonth')),
                ('reportyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reportyear')),
            ],
        ),
        migrations.AddField(
            model_name='reportmonth',
            name='reportperiodtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reportperiodtype'),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.province')),
            ],
        ),
        migrations.CreateModel(
            name='DataElementValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('synced', models.BooleanField(default=False)),
                ('dataElement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dataelement')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dataset')),
                ('healthFacility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthfacility')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.period')),
            ],
        ),
        migrations.AddField(
            model_name='dataelement',
            name='dataSet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.dataset'),
        ),
    ]
