from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    title = models.TextField(
        verbose_name='title'
    )

    picture = models.TextField(
        verbose_name='picture'
    )

    content = models.TextField(
        verbose_name='content'
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='updated',
        auto_now_add=True,
    )

    liked_by = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True,
        verbose_name='liked by'
    )

    shared_by = models.ManyToManyField(
        User,
        related_name='shared_posts',
        blank=True,
        verbose_name='shared by'
    )

    def __str__(self):
        return f"{self.user}: {self.content[:50]} ..."

    def share_post(self, user):

        if not self.shared_by.filter(id=user.id).exists():
            self.shared_by.create(user)
            self.save()
        return self

    def like_post(self, user):
        if not self.liked_by.filter(id=user.id).exists():
            self.liked_by.create(id=user.id)
            self.save()
        return self

    # def comments_under(self):
    #
    #     return self.comments.all()