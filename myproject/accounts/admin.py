from django.contrib import admin

from accounts.models import Comment, CustomUser, Post

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
