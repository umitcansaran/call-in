from rest_framework import status
from rest_framework.permissions import AllowAny

from project.api.permissions import IsOwnerOrReadOnlyOrgAndVol
from .serializers import OrganisationSerializer, RegisterOrganisationSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from .models import Organisation


class GetOrganisations(GenericAPIView):
    """
    GET: Get the list of all the organisations
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def get(self, request, *args, **kwargs):
        serializer = OrganisationSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)


class OrganisationCreateView(GenericAPIView):
    """
    POST: Create a new organisation
    """
    serializer_class = RegisterOrganisationSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organisation = serializer.create(serializer.validated_data)
        return Response(OrganisationSerializer(organisation).data)


class OrganisationGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Get the details of an organisation by providing the id of the organisation.
    PATCH: Update an organisation by id (only by organisation owner or admin).
    """
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsOwnerOrReadOnlyOrgAndVol]

    """
    DELETE: Delete an organisation by id (only by organisation owner or admin).
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Organisation was deleted', status=status.HTTP_204_NO_CONTENT)


class GetNGO(ListAPIView):
    """
    GET: Get the all the ngos
    """
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

    def get_queryset(self):
        ngos = self.queryset.filter(type='Non-profit organisation')
        return ngos


class GetProjects(ListAPIView):
    """
    GET: Get the all the projects
    """
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()

    def get_queryset(self):
        projects = self.queryset.filter(type='Project')
        return projects


class GetUserOrgs(ListAPIView):
    """
    GET: Get the all the organisations created by a specific user in chronological order
    """
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        queryset = Organisation.objects.all().order_by('created')
        user = self.kwargs.get('user_id')
        queryset = queryset.filter(user=user)
        return queryset
