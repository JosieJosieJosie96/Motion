from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import FriendRequest
from .serializers import FriendRequestSerializer


class FriendRequestListView(GenericAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get(self, request, *args, **kwargs):
        requests = FriendRequest.objects.filter(user_friends=request.user)
        serializer = self.get_serializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
