# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-07 16:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0043_auto_20170807_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 16, 4, 21, 617692)),
        ),
    ]
