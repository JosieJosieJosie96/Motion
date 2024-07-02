from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about_me = models.CharField(
        verbose_name='user description',
        max_length=1000,
        blank=True
    )

    follower = models.ManyToManyField(
        verbose_name='follower',
        to=settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True,
    )

    # liked_posts = models.ManyToManyField(
    #     verbose_name='liked posts',
    #     to=Posts,
    #     related_name='liked_by',
    #     blank=True,
    # )
    #
