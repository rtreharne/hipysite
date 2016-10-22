# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-22 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beekeeper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('twitter', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('linkedIn', models.URLField(null=True)),
                ('thumbnail', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=b'beekeeper_thumb')),
            ],
        ),
    ]