# Generated by Django 5.0.6 on 2024-07-05 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='followees'),
        ),
    ]
