from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile

# Dynamically get the custom user model
User = get_user_model()


"""
RegisterSerializer
------------------
Handles user registration.
- Accepts username, email, first/last name, date_of_birth, and profile_photo.
- Requires password + confirm password for validation.
- Automatically hashes password and creates a linked Profile.
"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  # confirm password

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "date_of_birth", "password", "password2"
        ]

    def validate(self, data):
        # Ensure both passwords match
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Remove confirm password before creating user
        validated_data.pop("password2")

        # Create user with Django's built-in create_user (hashes password)
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            date_of_birth=validated_data.get("date_of_birth"),
            profile_photo=validated_data.get("profile_photo"),
            password=validated_data.get("password"),
        )

        # Automatically create a Profile for the new user
        Profile.objects.create(user=user)
        return user


"""
LoginSerializer
---------------
Handles user authentication.
- Takes email + password.
- Validates credentials using Django's `authenticate`.
- If valid, returns JWT tokens (access + refresh).
"""
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return {
            "email": user.email,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


"""
ProfileSerializer
-----------------
Handles retrieving and updating profile information.
Keeps the profile data (bio, created_at) separate from the core User model.
"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["bio", "created_at"]
        read_only_fields = ["created_at"]
