# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-10 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_module_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='tagline',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]