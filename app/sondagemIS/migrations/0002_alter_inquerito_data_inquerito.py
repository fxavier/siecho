# Generated by Django 3.2.15 on 2022-11-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondagemIS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquerito',
            name='data_inquerito',
            field=models.DateField(auto_now=True),
        ),
    ]