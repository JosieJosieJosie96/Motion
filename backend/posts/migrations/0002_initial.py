# Generated by Django 5.0.6 on 2024-07-04 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='liked_by'),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_by',
            field=models.ManyToManyField(blank=True, related_name='shared_posts', to=settings.AUTH_USER_MODEL, verbose_name='shared by'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
