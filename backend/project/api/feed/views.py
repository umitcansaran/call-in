from datetime import datetime

from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from project.api.call.models import Call
from project.api.call.serializers import CallGetSerializer, CallGetOrgFeedSerializer
from project.api.event.models import Event
from project.api.event.serializers import EventSerializer, EventOrgFeedSerializer
from project.api.feed.serializers import ReadMeVolunteerSerializer, ReadMeOrganisationSerializer, ReadMeUserSerializer


class VolunteerFeedView(ListAPIView):
    """
    GET: Get the list of Events and Call (respectively Call options) the current user (volunteer) is participating
    """
    # serializer_class_Volunteer = ReadMeVolunteerSerializer
    serializer_class_Calls = CallGetSerializer
    serializer_class_Event = EventSerializer

    # def get_queryset_volunteer(self):
    #     return User.objects.get(id=self.request.user.id)

    def get_queryset_call(self):
        return Call.objects.filter(start_datetime__gte=datetime.now())
        # call_options__volunteers=self.request.user.volunteer.id)

    def get_queryset_event(self):
        return Event.objects.filter(start_datetime__gte=datetime.now())
        # participants=self.request.user.volunteer.id)

    def list(self, request, *args, **kwargs):
        # volunteer = self.serializer_class_Volunteer(self.get_queryset_volunteer()),
        call = self.serializer_class_Calls(self.get_queryset_call(), many=True)
        event = self.serializer_class_Event(self.get_queryset_event(), many=True)
        return Response({
            # "**VOLUNTEER**": volunteer.data,
            "**CALL**": call.data,
            "**EVENT**": event.data
        })


class VolunteerCalendarView(ListAPIView):
    """
    GET: Get the list of Events and Call (respectively Call options) the current user (volunteer) is participating
    """
    serializer_class_Calls = CallGetSerializer
    serializer_class_Event = EventSerializer

    def get_queryset_call(self):
        return Call.objects.filter(start_datetime__gte=datetime.now(),
                                   call_options__volunteers=self.request.user.volunteer.id)

    def get_queryset_event(self):
        return Event.objects.filter(start_datetime__gte=datetime.now(), participants=self.request.user.volunteer.id)

    def list(self, request, *args, **kwargs):
        call = self.serializer_class_Calls(self.get_queryset_call(), many=True)
        event = self.serializer_class_Event(self.get_queryset_event(), many=True)
        return Response({
            "**CALL**": call.data,
            "**EVENT**": event.data
        })


class ReadMeVolunteer(GenericAPIView):
    """
    GET: Get the profile of the current logged volunteer.
    """
    serializer_class = ReadMeVolunteerSerializer

    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = ReadMeVolunteerSerializer(user)
        return Response(serializer.data)


class OrganisationProfileAndFeedView(ListAPIView):
    """
    GET: Get the list of Events and Call (respectively Call options) of the logged in user (organisation)
    """
    serializer_class_Organisation = ReadMeOrganisationSerializer
    serializer_class_Calls = CallGetOrgFeedSerializer
    serializer_class_Event = EventOrgFeedSerializer

    def get_queryset_organisation(self):
        return User.objects.get(id=self.request.user.id)

    def get_queryset_call(self):
        return Call.objects.filter(start_datetime__gte=datetime.now(),
                                   organisation=self.request.user.organisation.id)

    def get_queryset_event(self):
        return Event.objects.filter(start_datetime__gte=datetime.now(), organisation=self.request.user.organisation.id)

    def list(self, request, *args, **kwargs):
        organisation = self.serializer_class_Organisation(self.get_queryset_organisation())
        call = self.serializer_class_Calls(self.get_queryset_call(), many=True)
        event = self.serializer_class_Event(self.get_queryset_event(), many=True)
        return Response({
            "**ORGANISATION PROFILE**": organisation.data,
            "**CALL**": call.data,
            "**EVENT**": event.data
        })


class ReadMeUser(GenericAPIView):
    """
    GET: Get the profile of the current logged in user
    """
    serializer_class = ReadMeUserSerializer

    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        serializer = ReadMeUserSerializer(user)
        return Response(serializer.data)
