# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20161023_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Description',
            new_name='Post',
        ),
    ]
