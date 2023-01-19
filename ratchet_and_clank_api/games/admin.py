from django.contrib import admin
from ratchet_and_clank_api.games.models import (
    Game
)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'release_date',)
