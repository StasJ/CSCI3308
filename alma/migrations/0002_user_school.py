# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='alma.School'),
            preserve_default=False,
        ),
    ]
