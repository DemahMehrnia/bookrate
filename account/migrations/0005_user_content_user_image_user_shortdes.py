# Generated by Django 4.0.1 on 2022-02-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_auth_token_user_created_at_user_is_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profileimages'),
        ),
        migrations.AddField(
            model_name='user',
            name='shortdes',
            field=models.TextField(null=True),
        ),
    ]
