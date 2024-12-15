from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.api.permissions import IsOwnerOrReadOnlyCallAndEvent
from .models import Event
from .serializers import EventSerializer


class GetEvents(GenericAPIView):
    """
    GET: Get the list of all the events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        serializer = EventSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)


class EventCreateView(GenericAPIView):
    """
    POST: Create a new events
    """
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.create(serializer.validated_data)
        return Response(EventSerializer(event).data)


class EventGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsOwnerOrReadOnlyCallAndEvent]
    """
    GET: Get the details of an event by providing the id of the event
    PATCH: Update an event by id (only by event owner (organisation owner) or admin)
    DELETE: Delete an event by id (only by event owner (organisation owner) owner or admin)
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Event was deleted', status=status.HTTP_204_NO_CONTENT)


class GetEventsByOrg(ListAPIView):
    serializer_class = EventSerializer

    """
    GET: Get the all the events from a specific organisation in chronological order
    """
    def get_queryset(self):
        queryset = Event.objects.all()
        org_id = self.kwargs.get('org_id')
        queryset = queryset.filter(organisation=org_id)
        return queryset
