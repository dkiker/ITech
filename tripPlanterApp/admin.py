from django.contrib import admin
from tripPlanterApp.models import Planner,Trip, Visit, Place

# Register your models here.

admin.site.register(Planner)
admin.site.register(Trip)
admin.site.register(Visit)
admin.site.register(Place)