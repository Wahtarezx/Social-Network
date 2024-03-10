from django.db import models
from django.contrib.auth.models import User


class Publications(models.Model):
    content = models.TextField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')

    def like_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'publication')


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300, null=True, blank=True)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE, related_name='comments')
