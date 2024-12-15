from django.contrib.auth.models import User
from django.db import models


class Volunteer(models.Model):

    # Attributes:
    first_name = models.CharField(
        verbose_name='first name',
        max_length=50
    )

    last_name = models.CharField(
        verbose_name='last name',
        max_length=50
    )

    location = models.TextField(
        verbose_name='location',
        max_length=50
    )

    facebook = models.URLField(
        verbose_name='facebook',
        max_length=100,
        blank=True,
        null=True
    )

    instagram = models.URLField(
        verbose_name='instagram',
        max_length=100,
        blank=True,
        null=True
    )

    linkedin = models.URLField(
        verbose_name='LinkedIn',
        max_length=100,
        blank=True,
        null=True
    )

    profile_picture = models.ImageField(
        verbose_name='profile picture',
        upload_to='volunteers/profile_pictures',
        null=True,
        blank=True
    )

    PUBLIC = 'public'
    PRIVATE = 'private'
    CONTROLLED = 'controlled'
    SECRET = 'secret'
    privacy_setting = models.CharField(
        verbose_name='privacy setting',
        max_length=100,
        choices=(
            (PUBLIC, PUBLIC),
            (PRIVATE, PRIVATE),
            (CONTROLLED, CONTROLLED),
            (SECRET, SECRET),
        ),
        default=PRIVATE
    )

    # Relations:
    user = models.OneToOneField(
        verbose_name='user',
        to=User,
        related_name='volunteer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
