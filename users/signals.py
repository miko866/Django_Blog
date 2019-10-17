from django.db.models.signals import post_save
from django.contrib.auth.models import User
# get signal and provide some task
from django.dispatch import receiver
from .models import Profile


# if user is Save came receiver and send signal and get in function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# kwargs accepts any added argument in function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # instance is User
    instance.profile.save()
