# Generated by Django 4.0.1 on 2022-01-28 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_moudles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_moudles.bookcategory'),
        ),
    ]
