# Generated by Django 4.2.16 on 2024-09-28 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='end_time',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AddField(
            model_name='availability',
            name='start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
