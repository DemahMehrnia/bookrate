# Generated by Django 4.0.1 on 2022-01-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0004_remove_books_writer'),
        ('blogs', '0003_blogs_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_moudles.books'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='content',
            field=models.TextField(default='ketab baz'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='short_description',
            field=models.CharField(default='ketab baz', max_length=300),
        ),
    ]