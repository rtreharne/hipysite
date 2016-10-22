# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'logo')),
                ('url', models.URLField(null=True)),
            ],
        ),
    ]
