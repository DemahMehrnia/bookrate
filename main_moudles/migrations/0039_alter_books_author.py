# Generated by Django 4.0.1 on 2022-02-02 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0038_alter_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authorrr', to='main_moudles.bookwriter'),
        ),
    ]
