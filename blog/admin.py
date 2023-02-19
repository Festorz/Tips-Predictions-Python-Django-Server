from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'intro', 'date_added']

    list_filter = ['likes', 'date_added']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
