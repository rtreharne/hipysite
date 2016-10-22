# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_hive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Hive')),
            ],
        ),
    ]
