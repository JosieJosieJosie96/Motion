from django.contrib.auth import get_user_model
from rest_framework import filters, permissions, status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.serializers import UserSerializer, UserUpdateSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class MeView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UserUpdateSerializer
        return UserSerializer

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']


class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'


class ListOfFollowers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def filter_queryset(self, queryset):
        return self.request.user.followers


class ListOfFollowing(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def filter_queryset(self, queryset):
        return self.request.user.followers


class FollowUnfollowUser(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_url_kwarg = 'user_id'

    def post(self, request, **kwargs):
        target_user = self.get_object()
        user = request.user
        if target_user in user.followers.all():
            user.followers.remove(target_user)
            return Response(self.get_serializer(instance=target_user).data)
        user.followers.add(target_user)
        return Response(self.get_serializer(instance=target_user).data)
