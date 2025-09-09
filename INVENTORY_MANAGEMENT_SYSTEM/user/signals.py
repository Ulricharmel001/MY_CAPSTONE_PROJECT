from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile



# user profile created automatically when each user created

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
