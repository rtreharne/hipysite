# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-07 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0039_auto_20170807_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 12, 56, 33, 413874)),
        ),
    ]
