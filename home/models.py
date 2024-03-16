from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from wagtail.models import Page


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    class Meta:
        ordering = ['-publish']
        
    def __str__(self):
        return self.title