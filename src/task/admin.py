from django.contrib import admin

from .models import Task, Star, Comment

admin.site.register(Task)
admin.site.register(Star)
admin.site.register(Comment)

