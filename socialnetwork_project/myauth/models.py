from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    interests = models.ManyToManyField('Interests', related_name='user_interests')
    subscriptions = models.ManyToManyField('self', related_name='subscriptions_set', symmetrical=False)
    subscribers = models.ManyToManyField('self', related_name='subscribers_set', symmetrical=False)

    def subscribers_count(self):
        return self.subscribers.count()

    def subscriptions_count(self):
        return self.subscriptions.count()


class Interests(models.Model):
    name = models.CharField(max_length=50, default='cats')
    description = models.TextField(max_length=200, null=True, blank=True)
