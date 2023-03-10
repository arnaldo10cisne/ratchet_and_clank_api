from django.contrib import admin
from ratchet_and_clank_api.characters.models import (
    Character
)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'first_appearance',)
