# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-02 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_video_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='uploade',
            new_name='uploaded',
        ),
    ]