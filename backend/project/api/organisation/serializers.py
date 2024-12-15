from rest_framework import serializers
from rest_framework.serializers import Serializer

from project.api.auth.serializers import User
from project.api.focus.serializers import FocusSerializer
from project.api.registration.serializer import RegistrationValidationSerializer
from .models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    focus = FocusSerializer()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Organisation
        fields = ['id', 'type', 'name', 'location', 'privacy_setting', 'profile_pic',
                  'description', 'website', 'phone', 'user', 'facebook', 'instagram',
                  'linkedin', 'focus', 'type']
        read_only_fields = ['type']
        extra_kwargs = {
            'user': {'required': False}
        }

    def get_type(self, organisation):
        return 'organisation'

    def create(self, validated_data):

        if 'user' not in validated_data:
            user_id = self.context.get('request').user.id
            validated_data['user'] = User.objects.get(pk=user_id)

        focus_data = validated_data.pop('focus')
        instance = super(OrganisationSerializer, self).create(validated_data)
        focus_data['organisation'] = instance
        focus_serializer = self.fields['focus']
        focus_serializer.create(focus_data)
        return instance

    def partial_update(self, instance, validated_data):
        focus_update = validated_data.pop('focus')
        focus = instance.focus
        focus_serializer = self.fields['focus']
        focus_serializer.update(focus, focus_update)
        return super().update(instance, validated_data)


class RegisterOrganisationSerializer(Serializer):
    validation = RegistrationValidationSerializer()
    organisation = OrganisationSerializer()

    def create(self, validated_data):
        registration_validation_data = validated_data.pop('validation')
        organisation_data = validated_data.pop('organisation')

        user = RegistrationValidationSerializer().save(registration_validation_data)
        organisation_data['user'] = user
        instance = OrganisationSerializer().create(organisation_data)
        return instance
