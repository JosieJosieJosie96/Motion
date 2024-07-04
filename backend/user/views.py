from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.serializers import UserSerializer, UserRegistrationSerializer

User = get_user_model()


class UserListView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    send_mail(
        'New User',
        f'Your code is {instance.code}.',
        'motionbackend1@gmail.com',
        [f'{instance.email}'],
        fail_silently=False,
    )


class RegistrationValidationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        if not email or not code:
            return Response({'message': 'Email and code are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_active == True:
            return Response({'message': 'You are already registered'}, status=status.HTTP_400_BAD_REQUEST)
        if user.code != code:
            return Response({'message': 'Your code is invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user.is_active = True
        user.save()

        return Response({'message': 'your registration is complete'}, status=status.HTTP_200_OK)


