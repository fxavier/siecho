# Generated by Django 3.2.13 on 2022-05-16 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistencia_tecnica', '0007_alter_indicador_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichaassistenciatecnica',
            name='indicadores',
        ),
        migrations.AddField(
            model_name='fichaassistenciatecnica',
            name='indicador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fichas', to='assistencia_tecnica.indicador'),
            preserve_default=False,
        ),
    ]
