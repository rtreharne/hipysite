# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-08 10:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0028_auto_20161208_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='event',
            name='stats',
            field=models.ImageField(blank=True, upload_to=b'stats'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 8, 10, 57, 8, 865993)),
        ),
    ]