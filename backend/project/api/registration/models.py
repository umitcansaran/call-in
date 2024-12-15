from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.api.helpers import code_generator


class UserProfile(models.Model):

    user = models.OneToOneField(
        verbose_name='user',
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    code = models.CharField(
        verbose_name='code',
        help_text='random code used for registration and for password reset',
        max_length=15,
        default=code_generator
    )

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, **kwargs):
        profile, created = UserProfile.objects.get_or_create(user=instance)
        if created:
            profile.save()
