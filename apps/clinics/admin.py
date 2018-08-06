from django.contrib import admin
from .models import Clinic, Event, Sport
# Register your models here.
admin.site.register(Clinic)
admin.site.register(Event)
admin.site.register(Sport)