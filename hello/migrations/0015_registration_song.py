# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_registration_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='song',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
