from django.contrib import admin

from posts.models import Comment, Group, Post, Follow


admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
