# Generated by Django 3.2.15 on 2022-10-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('si_stock', '0002_resumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumoVisualizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrumento', models.CharField(blank=True, max_length=255, null=True)),
                ('echo_misau', models.IntegerField(blank=True, null=True)),
                ('necessidade', models.IntegerField(blank=True, null=True)),
                ('stock_actual', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Resumo Visualizacao',
                'verbose_name_plural': 'Resumo Visualizacoes',
            },
        ),
    ]
