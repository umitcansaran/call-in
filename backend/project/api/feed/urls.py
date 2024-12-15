from django.urls import path

from project.api.feed.views import ReadMeVolunteer, VolunteerFeedView, OrganisationProfileAndFeedView, ReadMeUser, \
    VolunteerCalendarView

app_name = 'feed'

urlpatterns = [
    path('', VolunteerFeedView.as_view()),
    path('volunteer/me/', ReadMeVolunteer.as_view()),
    path('organisation/me/', OrganisationProfileAndFeedView.as_view()),
    path('user/me/', ReadMeUser.as_view()),
    path('volunteer/me/calendar/', VolunteerCalendarView.as_view())
]
