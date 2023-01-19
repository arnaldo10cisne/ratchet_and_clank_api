from django.db import models
from ratchet_and_clank_api.games.models import (
    Game
)


class Species(models.TextChoices):
    lombax = 'lombax'
    robot = 'robot'
    unknown = 'unknown'


class Character(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, choices=Species.choices)
    appearances = models.ManyToManyField(
        Game,
    )
    first_appearance = models.ForeignKey(
        Game,
        related_name='character_debuted',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
