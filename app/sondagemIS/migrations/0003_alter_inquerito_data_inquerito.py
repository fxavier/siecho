# Generated by Django 3.2.16 on 2023-02-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondagemIS', '0002_alter_inquerito_data_inquerito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquerito',
            name='data_inquerito',
            field=models.DateField(),
        ),
    ]
