# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-09 07:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0050_auto_20170809_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 9, 7, 13, 12, 670377)),
        ),
    ]
