
from __future__ import unicode_literals

from django.db import models


class Participant(models.Model):
    author = models.ForeignKey('account.User', null=True, related_name="author")
    helpers = models.ManyToManyField('account.User', related_name="helpers")
    post = models.ForeignKey('Post', null=True)


class Post (models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)


class Star(models.Model):
    owner = models.ForeignKey('account.User', null=True)
    post = models.ForeignKey('Post', null=True)


class Comment(models.Model):
    text = models.TextField(max_length=255)
    pub_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('account.User', null=True)
    post = models.ForeignKey('Post', null=True)


