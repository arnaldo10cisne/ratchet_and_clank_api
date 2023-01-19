from django.contrib import admin
from ratchet_and_clank_api.planets.models import (
    Planet
)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'first_appearance',)
