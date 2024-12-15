from django.urls import path
from .views import GetEvents, EventCreateView, \
    GetEventsByOrg, EventGetUpdateDeleteView

app_name = 'event'

urlpatterns = [
    path('new/', EventCreateView.as_view(), name='create_event'),
    path('', GetEvents.as_view(), name='list_events'),
    path('<int:id>/', EventGetUpdateDeleteView.as_view()),
    path('org/<int:org_id>/', GetEventsByOrg.as_view()),
]
