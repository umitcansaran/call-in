from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.api.bookmark.models import BookmarkModel
from project.api.bookmark.serializers import BookmarkModelSerializer
from project.api.call.serializers import CallGetSerializer
from project.api.event.serializers import EventSerializer

from project.api.event.models import Event
from project.api.call.models import Call


class ListBookmarkView(GenericAPIView):
    """
    GET: List all the 'events' and 'calls'
    """

    def get(self, request, *args, **kwargs):
        results = list()
        results += self.getListCall()
        results += self.getListEvent()
        return Response(results, status=status.HTTP_200_OK)

    def getListCall(self):
        user = self.request.user
        if hasattr(user, 'volunteer'):
            queryset = Call.objects.filter(bookmarks__volunteer__id=self.request.user.volunteer.id)
        elif hasattr(user, 'organisation'):
            queryset = Call.objects.filter(bookmarks__organisation__id=self.request.user.organisation.id)
        else:
            raise Exception('User not set up properly set up')
        serializer = CallGetSerializer(queryset, many=True)
        return serializer.data

    def getListEvent(self):
        user = self.request.user
        if hasattr(user, 'volunteer'):
            queryset = Event.objects.filter(bookmarks__volunteer__id=self.request.user.volunteer.id)
        elif hasattr(user, 'organisation'):
            queryset = Event.objects.filter(bookmarks__organisation__id=self.request.user.organisation.id)
        else:
            raise Exception('User not set up properly set up')
        serializer = EventSerializer(queryset, many=True)
        return serializer.data


class GetAllBookmarkByIdView(ListAPIView):
    """
    GET: List all the 'events' and 'calls' by id
    """
    serializer_class = CallGetSerializer
    serializer_class_event = EventSerializer

    def get_queryset_call(self, volunteer, organisation):
        if volunteer:
            return Call.objects.filter(bookmarks__volunteer__id=volunteer.id)

        if organisation:
            return Call.objects.filter(bookmarks__organisation__id=organisation.id)

    def get_queryset_event(self, volunteer, organisation):
        if volunteer:
            return Event.objects.filter(bookmarks__volunteer__id=volunteer.id)

        if organisation:
            return Event.objects.filter(bookmarks__organisation__id=organisation.id)

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])
        volunteer = user.volunteer if hasattr(user, 'volunteer') else None
        organisation = user.organisation if hasattr(user, 'organisation') else None

        if volunteer and organisation:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

        call = self.serializer_class(self.get_queryset_call(volunteer, organisation), many=True).data
        event = self.serializer_class_event(self.get_queryset_event(volunteer, organisation), many=True).data
        results = list()
        results += call
        results += event
        return Response(results, status=status.HTTP_200_OK)


class PostDeleteBookmarkCallByIdView(CreateAPIView, DestroyAPIView):
    """"
    POST AND DELETE: the bookmarked calls by id
    """
    model = BookmarkModel
    serializer_class = BookmarkModelSerializer
    queryset = BookmarkModel.objects.all()
    lookup_url_kwarg = 'call_id'
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        call = get_object_or_404(Call, id=kwargs[PostDeleteBookmarkCallByIdView.lookup_url_kwarg])
        user = request.user
        volunteer = user.volunteer if hasattr(user, 'volunteer') else None
        organisation = user.organisation if hasattr(user, 'organisation') else None

        if volunteer and organisation:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

        BookmarkModel.objects.get_or_create(volunteer=volunteer, organisation=organisation, call=call)
        return Response('Yupi, you bookmark the call', status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        call = get_object_or_404(Call, id=kwargs[PostDeleteBookmarkCallByIdView.lookup_url_kwarg])
        user = request.user
        volunteer = user.volunteer if hasattr(user, 'volunteer') else None
        organisation = user.organisation if hasattr(user, 'organisation') else None

        if volunteer and organisation:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

        bookmarks = BookmarkModel.objects.filter(volunteer=volunteer, organisation=organisation, call=call)
        if len(bookmarks) > 0:
            for bookmark in bookmarks:
                self.perform_destroy(bookmark)
        return Response('This bookmark of this call has been deleted', status=status.HTTP_201_CREATED)


class PostDeleteBookmarkEventByIdView(CreateAPIView, DestroyAPIView):
    """"
    POST AND DELETE: the events by id
    """
    model = BookmarkModel
    serializer_class = BookmarkModelSerializer
    queryset = BookmarkModel.objects.all()
    lookup_url_kwarg = 'event_id'
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=kwargs[PostDeleteBookmarkEventByIdView.lookup_url_kwarg])
        user = request.user
        volunteer = user.volunteer if hasattr(user, 'volunteer') else None
        organisation = user.organisation if hasattr(user, 'organisation') else None

        if volunteer and organisation:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
        BookmarkModel.objects.get_or_create(volunteer=volunteer, organisation=organisation, event=event)
        return Response("Yupi, you bookmark the event", status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        event = get_object_or_404(Event, id=kwargs[PostDeleteBookmarkEventByIdView.lookup_url_kwarg])
        user = request.user
        volunteer = user.volunteer if hasattr(user, 'volunteer') else None
        organisation = user.organisation if hasattr(user, 'organisation') else None

        if volunteer and organisation:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
        bookmarks = BookmarkModel.objects.filter(volunteer=volunteer, organisation=organisation, event=event)
        if len(bookmarks) > 0:
            for bookmark in bookmarks:
                self.perform_destroy(bookmark)

        return Response("The bookmark of this event has been deleted", status=status.HTTP_201_CREATED)
