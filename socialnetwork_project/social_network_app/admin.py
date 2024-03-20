from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from social_network_app.models import Publications, Reposts


class RepostsInline(GenericTabularInline):
    model = Reposts
    extra = 1


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    inlines = [
        RepostsInline,
    ]
    list_display = ('pk', 'content_short', 'like_count', 'pub_date', 'user', 'image')
    ordering = 'pk',
    search_fields = 'content', 'user__username'
    fieldsets = [
        (None, {
            'fields': ('content', 'image'),
        }),
        ('extra info', {
            'fields': ('user',),
            'classes': ('collapse',)
        })
    ]

    def content_short(self, obj: Publications) -> str:
        if len(obj.content) < 50:
            return obj.content
        return obj.content[:50] + '...'

    def get_queryset(self, request):
        return Publications.objects.select_related('user').prefetch_related('reposts')
