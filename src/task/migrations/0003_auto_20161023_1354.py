# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20161023_1349'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Participant',
        ),
    ]
