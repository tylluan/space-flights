from django.contrib import admin
from .form import FlightsForm, TouristsForm
from .models import Flights, Tourists


class FlightsAdmin(admin.ModelAdmin):
    form = FlightsForm
    view_on_site = False


class TouristsAdmin(admin.ModelAdmin):
    form = TouristsForm
    view_on_site = False


admin.site.register(Flights, FlightsAdmin)
admin.site.register(Tourists, TouristsAdmin)