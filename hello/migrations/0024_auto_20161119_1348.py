# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0023_auto_20161119_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 13, 47, 54, 7579)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
