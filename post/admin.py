from django.contrib import admin

from .models import Section, Post, Comment

admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Comment)
