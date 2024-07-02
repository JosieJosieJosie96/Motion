from django.contrib import admin
from backend.posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    list_filter = ['user']
    search_fields = ['title']
    ordering = ['title']


admin.site.register(Post, PostAdmin)
