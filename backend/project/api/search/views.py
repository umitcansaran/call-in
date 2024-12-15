import coreapi
from django.db.models import Q
from rest_framework import status

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from project.api.call.models import Call
from project.api.call.serializers import CallGetSerializer
from project.api.event.models import Event
from project.api.event.serializers import EventSerializer
from project.api.organisation.models import Organisation
from project.api.organisation.serializers import OrganisationSerializer
from project.api.volunteer.models import Volunteer
from project.api.volunteer.serializers import VolunteerSerializer


class SearchView(GenericAPIView):
    """"
    GET: Search for 'event', 'call' or 'volunteer'.{type: 'volunteer', 'search_string': 'interest'}
    """

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("search_string",
                          required=False,
                          location='query',
                          description='Search events, calls, volunteers'),
            coreapi.Field("search_location",
                          required=False,
                          location='query',
                          description='Location of the events, calls, volunteers'),
            coreapi.Field("volunteer_interest",
                          required=False,
                          location='query',
                          description='Define the interests you are looking for in your volunteers'),
        ]
    )

    def get(self, request, *args, **kwargs):
        search_string = self.request.query_params.get('search_string', None)
        volunteer_interest = self.request.query_params.get('volunteer_interest', None)
        search_location = self.request.query_params.get('search_location', None)
        results = list()
        results += self.searchVolunteers(search_string, volunteer_interest, search_location)
        results += self.searchCalls(search_string, search_location)
        results += self.searchEvents(search_string, search_location)
        results += self.searchOrganisations(search_string, search_location, volunteer_interest)
        return Response(results, status=status.HTTP_200_OK)

    def searchVolunteers(self, search_string, volunteer_interest, search_location):
        queryset = Volunteer.objects.all()
        queries = []
        if search_string:
            queries.append(Q(first_name__icontains=search_string))
            queries.append(Q(last_name__icontains=search_string))

        if search_location:
            queries.append(Q(location__icontains=search_location))

        if volunteer_interest:
            interests = volunteer_interest.split(',')

            if 'social' in interests:
                queries.append(Q(interests__social__icontains=search_string))

            if 'languages' in interests:
                queries.append(Q(interests__languages__icontains=search_string))

            if 'sports' in interests:
                queries.append(Q(interests__sports__icontains=search_string))

            if 'arts_culture' in interests:
                queries.append(Q(interests__arts_culture__icontains=search_string))

            if 'coaching' in interests:
                queries.append(Q(interests__coaching__icontains=search_string))

            if 'food' in interests:
                queries.append(Q(interests__food__icontains=search_string))

            if 'politics' in interests:
                queries.append(Q(interests__politics__icontains=search_string))

            if 'items' in interests:
                queries.append(Q(interests__items__icontains=search_string))

        if len(queries):
            query = queries.pop()
            # Or the Q object with the ones remaining in the list
            for item in queries:
                query |= item
            queryset = queryset.filter(query)

        serializer = VolunteerSerializer(queryset, many=True)
        return serializer.data

    def searchCalls(self, search_string, search_location):
        queryset = Call.objects.all()
        if search_string:
            queryset = queryset.filter(Q(
                Q(title__icontains=search_string) |
                Q(description__icontains=search_string)
            ))
        if search_location:
            queryset = queryset.filter(Q(
                Q(location__icontains=search_location)
            ))
        serializer = CallGetSerializer(queryset, many=True)

        return serializer.data

    def searchEvents(self, search_string, search_location):
        queryset = Event.objects.all()
        if search_string:
            queryset = queryset.filter(Q(
                Q(title__icontains=search_string)
            ))
        if search_location:
            queryset = queryset.filter(Q(
                Q(location__icontains=search_location)
            ))
        serializer = EventSerializer(queryset, many=True)
        return serializer.data

    def searchOrganisations(self, search_string, search_location, organisation_focus):
        queryset = Organisation.objects.all()
        queries = []
        if search_string:
            queries.append(Q(name__icontains=search_string))

        if search_location:
            queries.append(Q(location__icontains=search_location))

        if organisation_focus:
            interests = organisation_focus.split(',')

            if 'social' in interests:
                queries.append(Q(focus__social__icontains=search_string))

            if 'languages' in interests:
                queries.append(Q(focus__languages__icontains=search_string))

            if 'sports' in interests:
                queries.append(Q(focus__sports__icontains=search_string))

            if 'arts_culture' in interests:
                queries.append(Q(focus__arts_culture__icontains=search_string))

            if 'coaching' in interests:
                queries.append(Q(focus__coaching__icontains=search_string))

            if 'food' in interests:
                queries.append(Q(focus__food__icontains=search_string))

            if 'politics' in interests:
                queries.append(Q(focus__politics__icontains=search_string))

            if 'items' in interests:
                queries.append(Q(focus__items__icontains=search_string))

        if len(queries):
            query = queries.pop()
            # Or the Q object with the ones remaining in the list
            for item in queries:
                query |= item
            queryset = queryset.filter(query)

        serializer = OrganisationSerializer(queryset, many=True)
        print()
        return serializer.data
