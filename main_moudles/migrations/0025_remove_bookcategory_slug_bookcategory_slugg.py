# Generated by Django 4.0.1 on 2022-02-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0024_alter_bookcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='slug',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='slugg',
            field=models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True),
        ),
    ]
