# Generated by Django 4.0.1 on 2022-01-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0005_books_image_books_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.FileField(null=True, upload_to='bookimages'),
        ),
    ]
