# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20161101_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('DN', 'Do now'), ('WD', 'Will do')], default='WD', max_length=2),
        ),
    ]
