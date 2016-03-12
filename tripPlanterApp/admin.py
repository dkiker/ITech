from django.contrib import admin
from tripPlanterApp.models import Planner,Trip, Visit, Place

class PlannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')

class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'locationSlug':('location',)}
    list_display = ('name', 'type', 'location', 'description')

class TripAdmin(admin.ModelAdmin):
    list_display = ('planner', 'title')

class VisitAdmin(admin.ModelAdmin):
    list_display = ('trip', 'place')

admin.site.register(Planner, PlannerAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Visit, VisitAdmin)
