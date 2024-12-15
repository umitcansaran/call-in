from django.contrib import admin

# Register your models here.
from .models import Event

app_name = 'project.api.event'

admin.site.register(Event)
