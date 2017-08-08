# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.Module'),
        ),
        migrations.AddField(
            model_name='element',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
