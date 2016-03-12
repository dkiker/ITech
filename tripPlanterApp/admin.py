from django.contrib import admin
from tripPlanterApp.models import Planner,Trip, Visit, Place

# Register your models here.

# Add in this class to customized the Admin Interface
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'locationSlug':('location',)}

admin.site.register(Planner)
admin.site.register(Trip)
admin.site.register(Visit)
admin.site.register(Place, PlaceAdmin)