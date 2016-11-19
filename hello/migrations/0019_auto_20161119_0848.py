# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 08:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0018_auto_20161119_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='department',
            field=models.CharField(choices=[(b'BIOLOGY', b'Bilogy'), (b'EXTERNAL', b'External group/organisation'), (b'OTHER', b'Other')], default=b'OTHER', max_length=25),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 8, 48, 48, 522428)),
        ),
    ]
