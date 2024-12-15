from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializer import RegistrationSerializer, RegistrationValidationSerializer


class RegistrationView(GenericAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            new_user = serializer.save(serializer.validated_data)
            return Response(self.get_serializer(new_user).data)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationValidationView(GenericAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = RegistrationValidationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(
            serializer.validated_data,
        )
        return Response(self.get_serializer(user).data)
