from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from project.api.focus.serializers import FocusSerializer


class ReadFocus(GenericAPIView):
    serializer_class = FocusSerializer
    permission_classes = [IsAuthenticated]
