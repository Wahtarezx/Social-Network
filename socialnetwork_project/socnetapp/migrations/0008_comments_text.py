# Generated by Django 5.0.2 on 2024-03-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socnetapp', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='text',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]