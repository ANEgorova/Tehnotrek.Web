from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, unique=False, null=True, blank=False)
    username = models.CharField(max_length=255, unique=True, null=True, blank=False)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    text = models.TextField(max_length=255, null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)
    done_tasks = models.IntegerField(default=0)
    will_do_task = models.IntegerField(default=0)

