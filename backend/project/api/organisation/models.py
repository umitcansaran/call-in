from django.contrib.auth.models import User
from django.db import models


class Organisation(models.Model):

    # Attributes:
    name = models.CharField(
        verbose_name='name',
        max_length=200
    )

    NGO = 'Non-profit organisation'
    PROJECT = 'Project'
    type = models.CharField(
        verbose_name='type',
        max_length=100,
        choices=(
            (NGO, NGO),
            (PROJECT, PROJECT),
        ),
        default=NGO
    )

    PUBLIC = 'public'
    PRIVATE = 'private'
    CONTROLLED = 'controlled'
    SECRET = 'secret'
    privacy_setting = models.CharField(
        verbose_name='Privacy setting',
        max_length=100,
        choices=(
            (PUBLIC, PUBLIC),
            (PRIVATE, PRIVATE),
            (CONTROLLED, CONTROLLED),
            (SECRET, SECRET),
        ),
        default=PRIVATE
    )

    profile_pic = models.ImageField(
        upload_to='media-files/organisation/images',
        verbose_name='image',
        blank=True,
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

    document = models.FileField(
        upload_to='media-files/organisation/file',
        verbose_name='document',
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
        null=True
    )

    location = models.CharField(
        max_length=200
    )

    description = models.TextField(
        verbose_name='description'
    )

    website = models.CharField(
        max_length=200,
        blank=True
    )

    phone = models.CharField(
        max_length=200
    )

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    terms_of_services = models.BooleanField(
        choices=BOOL_CHOICES,
        default=False
    )

    # Relations:
    user = models.OneToOneField(
        verbose_name='user',
        to=User,
        related_name='organisation',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.name} - {self.user}'
