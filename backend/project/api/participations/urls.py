from django.urls import path
from .views import ParticipationsListView, ParticipantsView

app_name = 'participations'

urlpatterns = [
    path('<int:volunteer_id>/', ParticipationsListView.as_view()),
    path('event/<int:event_id>/', ParticipantsView.as_view()),
]
