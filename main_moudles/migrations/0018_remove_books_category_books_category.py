# Generated by Django 4.0.1 on 2022-02-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0017_books_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='category',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ManyToManyField(null=True, related_name='bookcat', to='main_moudles.bookcategory'),
        ),
    ]
