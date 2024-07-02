from rest_framework import serializers

from user.serializers import UserSerializer
from .models import FriendRequest



class FriendRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_friends = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id', 'user', 'user_friends', 'state']
