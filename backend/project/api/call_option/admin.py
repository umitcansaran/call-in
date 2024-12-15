from django.contrib import admin

from .models import CallOption


app_name = 'project.api.call_option'

admin.site.register(CallOption)
