from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from account.models import CustomUser


class UserSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration that handles password validation and user creation.

    Requires username, email, password and password confirmation.
    Ensures passwords match and meet Django's password validation requirements.
    """
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Ensure passwords match and meet Django's password validation requirements.
        """
        password = data.get('password', '')
        password2 = data.get('password2', '')
        validate_password(password)
        if password != password2:
            raise serializers.ValidationError("Two password fields do not match.")
        return data

    def create(self, validated_data) -> CustomUser:
        """
        Create a new user instance with validated data.
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
