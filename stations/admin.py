from django.contrib import admin
from stations.models import *

# Register your models here.
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'neighbors', 'arrival_popularity', 'departure_popularity')
admin.site.register(Station, StationAdmin)
