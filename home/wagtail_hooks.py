from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from taggit.models import Tag
from wagtail.admin.panels import FieldPanel

from .models import Post


class PostAdmin(ModelAdmin):
    model = Post
    base_url_path = 'Postadmin'
    menu_label = 'Post'
    menu_icon = 'pilcrow'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('title','slug','body','publish','created','updated','author', 'category')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('publish', 'author','category')
    ordering = ['-publish']

modeladmin_register(PostAdmin)

class TagsModelAdmin(ModelAdmin):
    Tag.panels = [FieldPanel("name")]
    model = Tag
    menu_label = "Tags"
    menu_icon = "tag"
    menu_order = 200
    list_display = ['name', 'slug']
    search_fields = ('name',)

modeladmin_register(TagsModelAdmin)