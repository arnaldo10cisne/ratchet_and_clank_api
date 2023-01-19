from django.db import models
from ratchet_and_clank_api.games.models import (
    Game,
)
from ratchet_and_clank_api.characters.models import (
    Character,
)


class Planet(models.Model):
    name = models.CharField(max_length=255)
    first_appearance = models.ForeignKey(
        Game,
        related_name='planet_debuted',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    appearances = models.ManyToManyField(
        Game,
    )
    characters = models.ManyToManyField(
        Character,
    )
