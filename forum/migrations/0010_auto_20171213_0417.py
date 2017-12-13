# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_post_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=forum.models.attachment_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
