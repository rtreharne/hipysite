# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-13 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0052_auto_20170809_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='flyer',
            field=models.ImageField(blank=True, upload_to=b'flyers'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 13, 37, 42, 604705)),
        ),
    ]