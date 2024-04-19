from django.db import models
from myauth.models import Interests


class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='advertisement/images', null=True, blank=True)
    interests = models.ManyToManyField('myauth.Interests', related_name='advertisement_interests')
