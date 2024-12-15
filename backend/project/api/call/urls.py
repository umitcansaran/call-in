from django.urls import path
from project.api.call.views import GetAllCalls, CreateCall, GetUpdateDeleteCall, GetListCallOfVol

app_name = 'call'

urlpatterns = [
    path('', GetAllCalls.as_view()),
    path('new/', CreateCall.as_view()),
    path('<int:id>/', GetUpdateDeleteCall.as_view()),
    path('vol/<int:vol_id>/', GetListCallOfVol.as_view())
]
