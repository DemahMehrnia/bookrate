# Generated by Django 4.0.1 on 2022-01-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogs_book_blogs_content_blogs_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
