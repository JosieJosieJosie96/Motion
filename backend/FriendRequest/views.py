from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import FriendRequest
from .serializers import FriendRequestSerializer

User = get_user_model()


class FriendRequestListView(GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get(self, request, *args, **kwargs):
        friend_requests = FriendRequest.objects.filter(user_friends=request.user)
        serializer = self.get_serializer(friend_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        to_user_id = request.data.get('to_user_id')
        if not to_user_id:
            return Response({'to_user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            to_user = User.objects.get(pk=to_user_id)
        except User.DoesNotExist:
            return Response({'to_user_id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        FriendRequest.objects.create(user=request.user, user_friends=to_user, status='pending')
        return Response({'status': 'friend request sent'}, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None):
        if not pk:
            return Response({'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend_request = FriendRequest.objects.get(pk=pk)
        except FriendRequest.DoesNotExist:
            raise NotFound('FriendRequest not found')

        friend_request.state = 'accepted'
        friend_request.save()
        return Response({'status': 'friend request accepted'}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        if not pk:
            return Response({'pk is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend_request = FriendRequest.objects.get(pk=pk)
        except FriendRequest.DoesNotExist:
            raise NotFound('FriendRequest not found')

        friend_request.delete()
        return Response({'status': 'friend request deleted'}, status=status.HTTP_204_NO_CONTENT)


class FriendListView(GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(user=self.request.user, state='accepted')

    def get(self, request, *args, **kwargs):
        friends = self.get_queryset()
        serializer = self.get_serializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
