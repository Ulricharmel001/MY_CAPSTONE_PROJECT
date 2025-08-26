from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


"""
Custom User Manager
-------------------
This manager handles the creation of both normal users and superusers.
By default, Django requires a username, but here we want to use `email` as the login field.
"""
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.
        email is required and normalized (lowercase, trimmed).
        password` is hashed using Django’s built-in security system.
        """
        if not email:
            raise ValueError("The Email field must be there")
        email = self.normalize_email(email)  # standardize email format
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hash password before saving
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser (admin).
        - Sets `is_staff`, `is_superuser`, and `is_active` to True by default.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


"""
Custom User Model
-----------------
We extend Django’s `AbstractUser` to customize authentication:
- Replace `username` with `email` as the unique login field.
- Still keep `first_name` and `last_name` from AbstractUser.
- Add optional fields like `date_of_birth` and `profile_photo`.
"""
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # still required for uniqueness
    email = models.EmailField(unique=True)  # email must be unique
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    # Tell Django to use email as the primary login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    # Link the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email


"""
Profile Model
-------------
A one-to-one relationship with `CustomUser` to hold extra profile data.
This keeps the user model clean while allowing profile expansion.
"""
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def full_name(self):
        """Return the full name of the related user."""
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"Profile of {self.user.email}"
