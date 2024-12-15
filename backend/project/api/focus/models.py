from django.db import models
from project.api.volunteer.models import Volunteer
from project.api.organisation.models import Organisation


class Focus(models.Model):
    organisation = models.OneToOneField(
        verbose_name='organisation',
        to=Organisation,
        related_name='focus',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    volunteer = models.OneToOneField(
        verbose_name='volunteer',
        to=Volunteer,
        related_name='interests',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    social = models.CharField(
        verbose_name='social',
        max_length=150,
        blank=True
    )

    languages = models.CharField(
        verbose_name='languages',
        max_length=150,
        blank=True
    )

    sports = models.CharField(
        verbose_name='sports',
        max_length=150,
        blank=True
    )

    arts_culture = models.CharField(
        verbose_name='arts & culture',
        max_length=150,
        blank=True
    )

    coaching = models.CharField(
        verbose_name='coaching',
        max_length=150,
        blank=True
    )

    food = models.CharField(
        verbose_name='food',
        max_length=150,
        blank=True
    )

    politics = models.CharField(
        verbose_name='politics',
        max_length=150,
        blank=True
    )

    items = models.CharField(
        verbose_name='items',
        max_length=150,
        blank=True
    )

    def __str__(self):
        if self.organisation:
            return f'Focus of: {self.organisation}'
        elif self.volunteer:
            return f'Interests of: {self.volunteer}'
