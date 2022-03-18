# Generated by Django 4.0.1 on 2022-01-31 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0011_alter_books_image_alter_bookwriter_image'),
        ('blogs', '0007_blogs_dislike_alter_blogs_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_moudles.books'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]