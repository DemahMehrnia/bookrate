# Generated by Django 4.0.1 on 2022-02-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0036_remove_bookwriter_dislike_remove_bookwriter_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookwriter',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]