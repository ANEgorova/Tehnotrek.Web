# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 13:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='helpers',
            field=models.ManyToManyField(related_name='helpers', to=settings.AUTH_USER_MODEL),
        ),
    ]
