# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-19 13:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0053_auto_20170813_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='hear',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 13, 59, 30, 149520)),
        ),
    ]
