from rest_framework.generics import ListCreateAPIView
from .models import FriendRequest
from .serializers import FriendRequestSerializer


class FriendRequestListView(ListCreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
