from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  
    created_at = models.DateTimeField(default=timezone.now)  # track creation time

    # method to get full name from related user
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"


# SIGNAL: Automatically create a profile when a new user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Only create when new user is registered
        Profile.objects.create(user=instance)


# SIGNAL: Save profile whenever user is updated
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
