from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FriendRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests')
    user_friends = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_display')
    state = models.CharField(max_length=50)
