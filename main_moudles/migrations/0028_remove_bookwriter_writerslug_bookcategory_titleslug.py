# Generated by Django 4.0.1 on 2022-02-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0027_remove_bookwriter_slug_bookwriter_writerslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookwriter',
            name='writerslug',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='titleslug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True),
        ),
    ]