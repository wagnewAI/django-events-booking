from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Always use this for custom user models

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing user details.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration (signup).
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
