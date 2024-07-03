from rest_framework import serializers
from .models import FriendRequest
from user.serializers import UserSerializer


class FriendRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_friends = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'user', 'user_friends', 'state']
