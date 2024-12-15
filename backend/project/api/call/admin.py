from django.contrib import admin

from .models import Call


app_name = 'project.api.call'

admin.site.register(Call)
