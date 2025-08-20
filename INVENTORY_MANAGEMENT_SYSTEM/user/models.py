from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extend Django's built-in AbstractUser to allow customization later
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure unique email
    date_of_birth = models.DateField(null=True, blank=True)  # Optional field
    profile_photo = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    # Use email instead of username for login
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # Username is still required for uniqueness

    def __str__(self):
        return self.email


# A separate Profile model linked to each user
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} Profile"


# SIGNAL: Automatically create a profile when a new user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only create when new user is registered
        Profile.objects.create(user=instance)


# SIGNAL: Save profile whenever user is updated
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
