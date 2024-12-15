from django.urls import path
from project.api.call_option.views import ListCallOptionsOfACall, GetUpdateDeleteCallOption

app_name = 'call_option'

urlpatterns = [
    path('call/<int:call_id>/', ListCallOptionsOfACall.as_view()),
    path('<int:id>/', GetUpdateDeleteCallOption.as_view())
]
