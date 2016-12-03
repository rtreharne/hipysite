# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0024_auto_20161119_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='song',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 13, 50, 36, 238800)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]