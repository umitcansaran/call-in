from django.urls import path
from .views import RegistrationView, RegistrationValidationView

app_name = 'registration'

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('validation/', RegistrationValidationView.as_view(), name='registration_validation'),
]
