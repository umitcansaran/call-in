from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/calls/', include('project.api.call.urls', namespace='call')),
    path('backend/docs/', include_docs_urls(title='call-in', public=False)),
    path('backend/api/auth/', include('project.api.auth.urls', namespace='authentication')),
    path('backend/api/organisations/', include('project.api.organisation.urls', namespace='organisations')),
    path('backend/api/events/', include('project.api.event.urls', namespace='event')),
    path('backend/api/registration/', include('project.api.registration.urls', namespace='registration')),
    path('backend/api/participations/', include('project.api.participations.urls', namespace='participations_event')),
    path('backend/api/search/', include('project.api.search.urls', namespace='search')),
    path('backend/api/feed/', include('project.api.feed.urls', namespace='feed')),
    path('backend/api/calloptions/', include('project.api.call_option.urls', namespace='call_option')),
    path('backend/api/volunteers/', include('project.api.volunteer.urls', namespace='volunteers')),
    path('backend/api/bookmarks/', include('project.api.bookmark.urls', namespace='bookmarks'))
]
