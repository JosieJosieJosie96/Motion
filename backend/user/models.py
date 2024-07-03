import random
import string

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


def code_generator(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


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

    liked_posts = models.ManyToManyField(verbose_name='liked posts', to='posts.Post', related_name='liked_by_users', blank=True)

    code = models.CharField(max_length=12, default=code_generator)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
