from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'qr_code', 'date']

admin.site.register(Event, EventAdmin)