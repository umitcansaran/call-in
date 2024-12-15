from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from project.api.call_option.models import CallOption
from project.api.call_option.serializers import CallOptionSerializerNotNested
from project.api.permissions import IsOwnerOrReadOnlyCallOption


class ListCallOptionsOfACall(ListCreateAPIView):
    """
    POST: Create a new option by providing the id of the call (only by call owner (organisation
    GET: List the call's options by providing the id of the relative call.
    """
    serializer_class = CallOptionSerializerNotNested

    def get_queryset(self):
        call_id = self.kwargs['call_id']
        return CallOption.objects.filter(call__id=call_id)


class GetUpdateDeleteCallOption(RetrieveUpdateDestroyAPIView):
    """
    GET: Get the details of an option by providing its id.
    PATCH: Update a call option by providing its id (only by call option owner (organisation owner) or admin).
    DELETE: Delete an event by id (only by call option owner (organisation owner) owner or admin).
    """
    serializer_class = CallOptionSerializerNotNested
    queryset = CallOption.objects.all()
    permission_classes = [IsOwnerOrReadOnlyCallOption]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["id"])
        self.check_object_permissions(self.request, obj)
        return obj
