from django.contrib import admin

# Register your models here.
from project.api.bookmark.models import BookmarkModel

app_name = 'project.api.bookmark'

admin.site.register(BookmarkModel)
