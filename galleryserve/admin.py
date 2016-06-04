from django.contrib import admin

from galleryserve import models
from django.conf import settings


class ItemInline(admin.StackedInline):
    model = models.Item
    extra = 1
    try:
        exclude = settings.GALLERYSERVE_EXCLUDE_FIELDS
    except:
        fieldsets = (
            (None, {'fields': (('image', 'alt', 'sort'),
                               ('url', 'video_url'), ('title', 'credit'), 'content')}),
        )


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
    list_display = ('title', 'parent_name')
    search_fields = ['title', ]

    def parent_name(self, obj):
        return obj.parent

    # Set child -> parent
    fieldsets = (
        (None, {'fields': (('title'), 'has_child', 'parent', 'content', 'height', 'width', 'random', 'resize',
                           'quality')}),
    )


admin.site.register(models.Gallery, GalleryAdmin)
