from django.contrib import admin
from .models import *

admin.sites.AdminSite.site_header = 'پنل مدیریت'


# inlines
class ImageInLine(admin.TabularInline):
    model = Images
    extra = 0


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


# Register your models here.
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['status', 'author', 'publish']
    search_fields = ['title', 'description']
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {"slug": ['title']}
    list_editable = ['status']
    # list_display_links = ['title']
    inlines = [ImageInLine, CommentInLine]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['phone', 'name', 'subject']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'created', 'active']
    list_filter = ['active', 'created']
    search_fields = ['name', 'body']
    list_editable = ['active']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['post', 'created', 'title']
