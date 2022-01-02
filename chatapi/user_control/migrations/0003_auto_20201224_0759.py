# Generated by Django 3.1 on 2020-12-24 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='favorite',
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite',
            field=models.ManyToManyField(related_name='user_favoured', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]