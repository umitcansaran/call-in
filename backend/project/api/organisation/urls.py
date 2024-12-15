from django.urls import path
from .views import GetOrganisations, OrganisationCreateView, OrganisationGetUpdateDeleteView, GetNGO, GetProjects, \
    GetUserOrgs

app_name = 'organisations'

urlpatterns = [
    path('', GetOrganisations.as_view()),
    path('new/', OrganisationCreateView.as_view()),
    path('<int:id>/', OrganisationGetUpdateDeleteView.as_view()),
    path('ngos/', GetNGO.as_view()),
    path('projects/', GetProjects.as_view()),
    path('user/<int:user_id>/', GetUserOrgs.as_view()),
]
