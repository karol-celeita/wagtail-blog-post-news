from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

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
    list_display = ('title','slug','body','publish','created','updated','author')
    search_fields = ('title', 'body', 'author__username')
    list_filter = ('publish', 'author')
    ordering = ['-publish']

modeladmin_register(PostAdmin)