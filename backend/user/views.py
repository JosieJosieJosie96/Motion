from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from user.serializer import UserSerializer

User = get_user_model()


class UserListView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
