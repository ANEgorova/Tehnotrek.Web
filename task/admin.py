from django.contrib import admin

from .models import Post, Star, Participant, Comment

admin.site.register(Post)
admin.site.register(Star)
admin.site.register(Participant)
admin.site.register(Comment)


