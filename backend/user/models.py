from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    users_following = models.ManyToManyField('self', related_name='following', blank=True, symmetrical=False,)
