# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 18:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_auto_20171109_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 18, 39, 16, 413049, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
