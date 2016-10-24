from __future__ import unicode_literals

from django.db import models

from django.conf import settings


class Article (models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_data = models.DateField(auto_now_add=True)

