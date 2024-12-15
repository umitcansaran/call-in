from rest_framework import serializers

from project.api.call_option.serializers import CallOptionSerializer
from project.api.organisation.serializers import OrganisationSerializer
from .models import Call


class CallGetSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer()
    call_options = CallOptionSerializer(many=True, required=False)
    type = serializers.SerializerMethodField()

    class Meta:
        model = Call
        fields = ['id', 'title', 'call_picture', 'organisation', 'created', 'start_datetime', 'end_datetime',
                  'location', 'description', 'must_be_approved', 'call_options', 'type']
        read_only_fields = ['organisation', 'call_options', 'type']
        ordering = ['start_datetime']

    def get_type(self, call):
        return 'call'


class CallGetOrgFeedSerializer(serializers.ModelSerializer):
    call_options = CallOptionSerializer(many=True, required=False)

    class Meta:
        model = Call
        fields = ['id', 'title', 'call_picture', 'organisation', 'created', 'start_datetime', 'end_datetime',
                  'location', 'description', 'must_be_approved', 'call_options']
        read_only_fields = ['id', 'title', 'call_picture', 'organisation', 'start_datetime', 'end_datetime',
                            'location', 'description', 'must_be_approved', 'call_options']
        ordering = ['start_datetime']


class CallPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ['title', 'call_picture', 'organisation', 'start_datetime', 'end_datetime',
                  'location', 'description', 'must_be_approved']
        read_only_fields = ['organisation']
        extra_kwargs = {
            'call_options': {'required': True}
        }

    def create(self, validated_data):
        validated_data['organisation'] = self.context.get('request').user.organisation
        instance = super(CallPostSerializer, self).create(validated_data)
        call_options = self.context.get('request').data['call_options']
        for option in call_options:
            option['call'] = instance.id
            serializer = CallOptionSerializer(data=option)
            serializer.is_valid()
            serializer.create(serializer.validated_data)
        return instance

    def partial_update(self, instance, validated_data):
        call_options_update = validated_data.pop('call_options')
        call_options = instance.call_options
        call_options_serializer = self.fields['call_options']
        call_options_serializer.update(call_options, call_options_update)
        return super().update(instance, validated_data)
