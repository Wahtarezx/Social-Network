from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from social_network_app.models import Publications, Reposts


class RepostsInline(GenericTabularInline):
    model = Reposts
    extra = 1


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    inlines = [
        RepostsInline,
    ]
    list_display = ('pk', 'content_short', 'like_count', 'pub_date', 'user', 'image_tag')
    ordering = 'pk',
    search_fields = 'content', 'user__username'
    fieldsets = [
        (None, {
            'fields': ('content', 'image',),
        }),
        ('extra info', {
            'fields': ('user', 'like_count'),
            'classes': ('collapse',)
        })
    ]

    readonly_fields = ['preview', 'like_count']

    def preview(self, obj):
        return mark_safe('<img src="{}" style="max-height: 200px; max-width: 200px;" />'.format(obj.image.url))

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:120px; max-height:120"/>'.format(obj.image.url))
        return 'No image'

    image_tag.short_description = 'Image'

    def content_short(self, obj: Publications) -> str:
        if len(obj.content) < 50:
            return obj.content
        return obj.content[:50] + '...'

    def get_queryset(self, request):
        return Publications.objects.select_related('user').prefetch_related('reposts')
