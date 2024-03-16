from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from wagtail.models import Page
from django.urls import reverse
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from .blocks import ImageText, Quote, List
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    body = StreamField([('photo', ImageChooserBlock()),
                        ('image_text', ImageText()),
                        ('h1', blocks.CharBlock()),
                        ('h2', blocks.CharBlock()),
                        ('h3', blocks.CharBlock()),
                        ('h4', blocks.CharBlock()),
                        ('h5', blocks.CharBlock()),
                        ('quote', Quote()),
                        ('link', blocks.URLBlock()),
                        ('list', List()),
                        ('email', blocks.EmailBlock()),
                        ('integer_number', blocks.IntegerBlock()),
                        ('float_number', blocks.FloatBlock()),
                        ('decimal_number', blocks.DecimalBlock()),
                        ('date', blocks.DateBlock()),
                        ('time', blocks.TimeBlock()),
                        ('date_with_time', blocks.DateTimeBlock()),
                        ('text', blocks.TextBlock()),
                        ('paragraph', blocks.RichTextBlock()),
                        ('quote_set', blocks.BlockQuoteBlock()),
                        ('document', DocumentChooserBlock()),
                        ('embed', EmbedBlock()),
                        
                        
                        ])
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    class Meta:
        ordering = ['-publish']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home:post_detail', args=[str(self.slug)])