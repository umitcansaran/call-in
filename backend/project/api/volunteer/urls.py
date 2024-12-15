from django.urls import path
from .views import GetVolunteers, VolunteerCreateView, VolunteerGetUpdateDeleteView, ConfirmCallVolunteer

app_name = 'volunteers'

urlpatterns = [
    path('', GetVolunteers.as_view()),
    path('new/', VolunteerCreateView.as_view()),
    path('<int:id>/', VolunteerGetUpdateDeleteView.as_view()),
    path('request/call/<int:call_option_id>/', ConfirmCallVolunteer.as_view()),
]
