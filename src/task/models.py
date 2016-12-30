# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Task (models.Model):
    author = models.ForeignKey('account.User', null=True, related_name="author")
    helpers = models.ManyToManyField('account.User', related_name="helpers", blank=True, swappable=False)
    title = models.CharField(max_length=500)
    text = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)
    task_statuses = [('DN', 'Do now'), ('WD', 'Will do')]
    status = models.CharField(max_length=2, choices=task_statuses, default='WD')

    def __unicode__(self):
        return u'{} от {}'.format(self.title, self.pub_data)

    #  View tasks in decrease order by create date
    class Meta:
        verbose_name = u'Task'
        verbose_name_plural = u'Tasks'
        ordering = ('pub_data',)


class Star(models.Model):
    owner = models.ForeignKey('account.User', null=True)
    post = models.ForeignKey('Task', null=True)


class Comment(models.Model):
    text = models.TextField(max_length=255)
    pub_data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('account.User', null=True)
    post = models.ForeignKey('Task', null=True)

