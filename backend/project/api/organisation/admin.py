from django.contrib import admin
from .models import Organisation

app_name = 'project.api.organisation'

admin.site.register(Organisation)
