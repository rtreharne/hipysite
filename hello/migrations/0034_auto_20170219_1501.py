# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-19 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0033_auto_20170118_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 19, 15, 1, 48, 626021)),
        ),
    ]
