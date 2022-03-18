# Generated by Django 4.0.1 on 2022-02-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0026_remove_bookcategory_slugg_bookwriter_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookwriter',
            name='slug',
        ),
        migrations.AddField(
            model_name='bookwriter',
            name='writerslug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True),
        ),
    ]