from django.db import models

from project.api.call.models import Call
from project.api.event.models import Event
from project.api.organisation.models import Organisation
from project.api.volunteer.models import Volunteer


class BookmarkModel(models.Model):

    event = models.ForeignKey(
        verbose_name='event',
        to=Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bookmarks'
    )
    call = models.ForeignKey(
        verbose_name='call',
        to=Call,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bookmarks'
    )
    organisation = models.ForeignKey(
        verbose_name='organisation',
        to=Organisation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='bookmarks'

    )
    volunteer = models.ForeignKey(
        verbose_name='volunteer',
        to=Volunteer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='bookmarks'
    )
