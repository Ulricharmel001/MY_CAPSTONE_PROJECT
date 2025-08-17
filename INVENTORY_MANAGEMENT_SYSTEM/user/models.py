from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Custom user manager to handle creation of regular and superusers
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with hashed password
        """
        if not email:
            raise ValueError("Email must be set")
        if not username:
            raise ValueError("Username must be set")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Securely hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a superuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)


# Custom user model with extra fields
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
