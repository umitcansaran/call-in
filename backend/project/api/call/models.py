from django.db import models
from project.api.organisation.models import Organisation


class Call(models.Model):

    title = models.CharField(
        verbose_name='title of the call',
        max_length=50
    )

    call_picture = models.ImageField(
        verbose_name='call picture',
        upload_to='call_pictures',
        null=True,
        blank=True
    )

    organisation = models.ForeignKey(
      verbose_name='organisation',
      to=Organisation,
      related_name='call',
      on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    start_datetime = models.DateTimeField(
        verbose_name='start of the call'
    )

    end_datetime = models.DateTimeField(
        verbose_name='end of the call'
    )

    location = models.CharField(
        verbose_name='location',
        max_length=50
    )

    description = models.CharField(
        verbose_name='description',
        max_length=150
    )

    must_be_approved = models.BooleanField(
        verbose_name='must be approved'
    )

    def __str__(self):
        return f'{self.title} [{self.organisation}]'
