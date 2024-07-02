from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
        read_only_fields = ('date_joined', 'last_login')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'code', 'password', 'password_repeat', 'first_name', 'last_name', 'email']

    def validate(self, attrs):
        password = attrs.get('password')
        password_repeat = attrs.get('password_repeat')

        if password != password_repeat:
            raise serializers.ValidationError({"password_repeat": "Passwords do not match."})

        return attrs

    def update(self, instance, validated_data):
        validated_data.pop('password_repeat')  # Remove password_repeat since it's not needed for user update
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
