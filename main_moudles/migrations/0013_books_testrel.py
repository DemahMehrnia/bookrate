# Generated by Django 4.0.1 on 2022-01-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0012_tttest'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='testrel',
            field=models.ManyToManyField(blank=True, related_name='fsdfafsfbooksreading', to='main_moudles.tttest'),
        ),
    ]
