# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 18:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20171109_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 18, 42, 6, 593762, tzinfo=utc)),
        ),
    ]