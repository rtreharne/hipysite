# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 13:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0022_auto_20161119_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='song',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 13, 45, 2, 344137)),
        ),
    ]