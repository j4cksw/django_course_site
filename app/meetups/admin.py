from django.contrib import admin
from .models import Location, Meetup, Participant

# Register your models here.
admin.site.register(Meetup)
admin.site.register(Location)
admin.site.register(Participant)
