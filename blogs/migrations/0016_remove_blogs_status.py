# Generated by Django 4.0.1 on 2022-02-03 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_blogs_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='status',
        ),
    ]