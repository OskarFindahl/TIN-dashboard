from django.contrib import admin
from .models import JobData, Spider

admin.site.register([JobData, Spider])


