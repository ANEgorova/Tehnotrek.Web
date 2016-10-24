from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True, null=True)
    avatar = models.FileField(upload_to='avatars', blank=True, null=True)
    text = models.TextField(max_length=255, null=True)
    friends = models.ManyToManyField('self')
    # task we can get from task.Participants