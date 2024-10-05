from accounts.models import Comment, CustomUser, Post
from django.contrib import admin

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
