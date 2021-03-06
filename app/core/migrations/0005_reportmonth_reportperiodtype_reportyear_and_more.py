# Generated by Django 4.0.3 on 2022-04-07 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_openmrs_designation_period_id'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='dataelementvalue',
            name='period',
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
    ]
