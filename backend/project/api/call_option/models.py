from django.db import models
from project.api.call.models import Call
from project.api.volunteer.models import Volunteer


class CallOption(models.Model):

    call = models.ForeignKey(
        to=Call,
        verbose_name='call',
        on_delete=models.CASCADE,
        related_name='call_options'
    )

    title = models.CharField(
        verbose_name='title',
        max_length=100
    )

    volunteers = models.ManyToManyField(
        to=Volunteer,
        verbose_name='volunteer participating',
        related_name='call_options',
        blank=True
    )

    def __str__(self):
        return f'{self.title} - Call: {self.call}'
