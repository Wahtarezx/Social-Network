from django.contrib import admin

from advertisement.models import Advertisement


class InterestsInline(admin.TabularInline):
    model = Advertisement.interests.through


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [InterestsInline,]
    list_display = ('pk', 'name', 'text_short', 'image')
    list_display_links = ('pk', 'name')
    ordering = 'pk',
    search_fields = 'name', 'text'
    fieldsets = [
        (None, {
            'fields': ('name', 'text',),
        }),
        ('Images', {
            'fields': ('image',),
        }),
    ]

    def text_short(self, obj : Advertisement) -> str:
        if len(obj.text) < 50:
            return obj.text
        return obj.text[:50] + '...'

    def get_queryset(self, request):
        return Advertisement.objects.prefetch_related('interests')
