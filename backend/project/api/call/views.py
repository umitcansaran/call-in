from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from project.api.call.models import Call
from project.api.call.serializers import CallGetSerializer, CallPostSerializer
from project.api.permissions import IsOwnerOrReadOnlyCallAndEvent


class GetAllCalls(ListAPIView):
    """
    GET: Get the list of all the calls.
    """
    serializer_class = CallGetSerializer
    queryset = Call.objects.all().order_by('-created')

    def get_queryset(self):
        queryset = Call.objects.all().order_by('-created')
        return queryset


class CreateCall(GenericAPIView):
    """
    POST: Create a new call.
    """
    serializer_class = CallPostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        call = serializer.create(serializer.validated_data)
        return Response(CallGetSerializer(call).data)


class GetUpdateDeleteCall(GenericAPIView):
    queryset = Call.objects.all()
    serializer_class = CallGetSerializer
    permission_classes = [IsOwnerOrReadOnlyCallAndEvent]

    """
    GET: Get the details of a call by providing the id of the call.
    """
    def get(self, request, **kwargs):
        call_id = self.kwargs.get('id')
        try:
            call = Call.objects.get(id=call_id)
            self.check_object_permissions(request, call)
        except Call.DoesNotExist:
            return Response(f'This call does not exist', status=status.HTTP_404_NOT_FOUND)
        serializer = CallGetSerializer(call)
        return Response(serializer.data)

    """
    PATCH: Update a call by id (only by call owner (organisation owner) or admin).
    """
    def patch(self, request, **kwargs):
        call_id = self.kwargs.get('id')
        try:
            call = Call.objects.get(id=call_id)
            self.check_object_permissions(request, call)
        except Call.DoesNotExist:
            return Response(f'This call does not exist', status=status.HTTP_404_NOT_FOUND)
        serializer = CallGetSerializer(instance=call, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    """
    DELETE: Delete a call by id (only by call owner (organisation owner) or admin).
    """
    def delete(self, request, **kwargs):
        call_id = self.kwargs.get('id')
        try:
            call = Call.objects.get(id=call_id)
            self.check_object_permissions(request, call)
        except Call.DoesNotExist:
            return Response(f'This call does not exist', status=status.HTTP_404_NOT_FOUND)
        if request.user.id == call.organisation.user.id or request.user.is_staff:
            call.delete()
            return Response('call deleted')
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class GetListCallOfVol(GenericAPIView):
    """
    GET: Get the list of all the calls a volunteer is participating.
    """
    queryset = Call.objects.all()
    serializer_class = CallPostSerializer

    def get(self, request, **kwargs):
        vol_id = self.kwargs.get('vol_id')
        calls = Call.objects.filter(call_options__volunteers=vol_id)
        serializer = CallGetSerializer(calls, many=True)
        return Response(serializer.data)
