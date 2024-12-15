from rest_framework import serializers
from django.contrib.auth.models import User

from project.api.organisation.serializers import OrganisationSerializer
from project.api.volunteer.serializers import VolunteerSerializer


class ReadMeVolunteerSerializer(serializers.ModelSerializer):
    volunteer = VolunteerSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'volunteer']


class ReadMeOrganisationSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'organisation']


class ReadMeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'volunteer', 'organisation']
