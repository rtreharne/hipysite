# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_registration_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 7, 47, 50, 610427)),
        ),
    ]
