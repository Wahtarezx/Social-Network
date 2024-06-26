# Generated by Django 5.0 on 2024-04-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myauth', '0003_customuser_subscribers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisement/images')),
                ('interests', models.ManyToManyField(related_name='advertisement_interests', to='myauth.interests')),
            ],
        ),
    ]
