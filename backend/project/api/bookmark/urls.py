from django.urls import path

from project.api.bookmark.views import ListBookmarkView, GetAllBookmarkByIdView, PostDeleteBookmarkCallByIdView, \
     PostDeleteBookmarkEventByIdView

app_name = 'bookmarks'

urlpatterns = [
     path('', ListBookmarkView.as_view()),
     path('<int:id>/', GetAllBookmarkByIdView.as_view()),
     path('calls/<int:call_id>/', PostDeleteBookmarkCallByIdView.as_view()),
     path('events/<int:event_id>/', PostDeleteBookmarkEventByIdView.as_view()),
]
