# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-26 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0063_auto_20171010_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 10, 55, 43, 40282)),
        ),
    ]
