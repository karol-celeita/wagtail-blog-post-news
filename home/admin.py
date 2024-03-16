from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','body','publish','created','updated','author']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-publish']
    list_filter = ['created','author']
    search_fields = ['title', 'body']