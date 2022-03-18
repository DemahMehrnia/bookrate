# Generated by Django 4.0.1 on 2022-01-31 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0006_blogs_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='blogdislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='bloglikes', to=settings.AUTH_USER_MODEL),
        ),
    ]