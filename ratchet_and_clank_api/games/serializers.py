from rest_framework import serializers
from ratchet_and_clank_api.games.models import (
    Game
)


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'name',
            'release_date',
        ]
