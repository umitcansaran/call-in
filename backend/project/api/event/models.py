from django.db import models
from project.api.organisation.models import Organisation
from project.api.volunteer.models import Volunteer


class Event(models.Model):
    title = models.CharField(
        max_length=100
    )
    picture = models.ImageField(
        upload_to='event/images',
        null=True, blank=True
    )
    organisation = models.ForeignKey(
        to=Organisation,
        related_name='event',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    start_datetime = models.DateTimeField(
        verbose_name='start of the event'
    )
    end_datetime = models.DateTimeField(
        verbose_name='end of the call'
    )
    location = models.CharField(
        max_length=200
    )
    description = models.TextField(
        max_length=500
    )
    participants = models.ManyToManyField(
        to=Volunteer,
        related_name='event',
        blank=True
    )
    must_be_approved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.title} [{self.organisation}]'

    class Meta:
        ordering = ['created']
