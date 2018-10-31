from django.contrib import admin

from djinn_pages.models import AllowedIFrameURL
from .models import MenuItem


class MenuItemAdminInline(admin.TabularInline):
    model = MenuItem


class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title', 'url', 'parent', )
    list_filter = ['parent', ]
    search_fields = ['title', 'url']
    inlines = [MenuItemAdminInline]

admin.site.register(MenuItem, MenuItemAdmin)


class AllowedIFrameURLAdmin(admin.ModelAdmin):

    list_display = ('url_name', 'url')

admin.site.register(AllowedIFrameURL, AllowedIFrameURLAdmin)
