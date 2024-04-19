from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Publications(models.Model):
    content = models.TextField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='publications')
    reposts = GenericRelation('Reposts')
    image = models.ImageField(upload_to='publications/images', null=True, blank=True)

    def like_count(self):
        return self.likes.count()

    def reposts_count(self):
        return self.reposts.count()


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='likes')
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'publication')


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=300, null=True, blank=True)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE, related_name='comments')
    reposts = GenericRelation('Reposts')


class Reposts(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reposts')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'id__in': [12, 14]})
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
