# Generated by Django 4.0.2 on 2022-02-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]