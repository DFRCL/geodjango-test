from django.contrib.gis import admin
from app.models import Venue, Area


class VenueAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'city', 'state', 'zip']
    list_filter = ['state', 'city']


class AreaAdmin(admin.OSMGeoAdmin):
    list_display = ['name']


admin.site.register(Venue, VenueAdmin)
admin.site.register(Area, AreaAdmin)
