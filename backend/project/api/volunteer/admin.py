from django.contrib import admin

# Register your models here.
from .models import Volunteer

app_name = 'project.api.volunteer'

admin.site.register(Volunteer)