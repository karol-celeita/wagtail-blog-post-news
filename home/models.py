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
from django.core.validators import MaxValueValidator, MinValueValidator #Star Rating
from taggit.managers import TaggableManager
from wagtail.snippets.models import register_snippet

@register_snippet
class Categories(models.Model):
    name = models.CharField(max_length= 50)
    slug = models.SlugField(max_length= 80)
    
    class Meta():
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"

    def __str__(self):
        return self.name

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
    
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.CASCADE, related_name='post_category')
    
    class Meta:
        ordering = ['-publish']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home:post_detail', args=[str(self.slug)])
    
    #rating average
    def get_average_rating_score (self):
        average_score = 0
        if self.reviews.count() > 0:
            total_score= sum([review.rating for review in self.reviews.all()])
            average_score = total_score/self.reviews.count()
        return round(average_score,1)
    
    #review count
    def get_review_count(self):
        return self.reviews.count()
    
class Review(models.Model):
    post = models.ForeignKey(Post, related_name = 'reviews', on_delete=models.CASCADE)
    author= models.CharField(max_length = 50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField (blank=True)
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ('-created',)
        
    def get_star_count(self):
        return range(self.rating)
    
    