# Generated by Django 5.0.2 on 2024-03-14 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network_app', '0004_publications_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='image',
        ),
    ]