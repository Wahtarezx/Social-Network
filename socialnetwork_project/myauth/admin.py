from django.contrib import admin
from django.core.mail import send_mail

from myauth.models import CustomUser
from advertisement.models import Advertisement


class InterestsInline(admin.StackedInline):
    model = CustomUser.interests.through


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [InterestsInline]
    fieldsets = [
        ('General info', {
            'fields': (
                'first_name', 'last_name', 'username', 'email',
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
            ),
        }),
    ]

    def send_advertisement_emails(self, request, queryset):
        for ad in Advertisement.objects.all():
            interests = ad.interests.all()

            users_with_matching_interests = set()
            for interest in interests:
                users_with_matching_interests.update(interest.user_interests.all())
            print(users_with_matching_interests)
            for user in users_with_matching_interests:
                subject = ad.name
                message = ad.text
                send_mail(subject, message, None, [user.email])

        self.message_user(request, "Письма успешно отправлены")

    send_advertisement_emails.short_description = "Отправить рекламные письма"

    actions = ['send_advertisement_emails']
