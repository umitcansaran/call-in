from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from project.api.call_option.models import CallOption
from project.api.permissions import IsOwnerOrReadOnlyOrgAndVol
from .models import Volunteer
from .serializers import VolunteerSerializer, RegisterVolunteerSerializer


class GetVolunteers(GenericAPIView):
    """
    GET: Get the list of all the volunteers
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    def get(self, request, *args, **kwargs):
        serializer = VolunteerSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)


class VolunteerCreateView(GenericAPIView):
    """
    POST: Create a new volunteer
    """
    serializer_class = RegisterVolunteerSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        volunteer = serializer.create(serializer.validated_data)
        return Response(VolunteerSerializer(volunteer).data)


class VolunteerGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Get the details of a volunteer by providing the id of the volunteer
    PATCH: Update a volunteer by id (only by volunteer owner or admin)
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsOwnerOrReadOnlyOrgAndVol]

    """
    DELETE: Delete a volunteer by id (only by volunteer owner or admin)
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='User was deleted', status=status.HTTP_204_NO_CONTENT)


class ConfirmCallVolunteer(GenericAPIView):
    """
    POST: Confirm a volunteer's participation in a Call (only by volunteer)
    """
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        call_option_id = self.kwargs.get('call_option_id')
        try:
            selected_call = CallOption.objects.get(id=call_option_id)
        except CallOption.DoesNotExist:
            raise Http404
        volunteer = Volunteer.objects.get(id=request.user.volunteer.id)
        selected_call.volunteers.add(volunteer)
        return Response('Your participation in the Call is confirmed', status.HTTP_200_OK)
