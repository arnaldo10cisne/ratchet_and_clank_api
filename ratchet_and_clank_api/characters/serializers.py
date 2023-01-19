from rest_framework import serializers
from ratchet_and_clank_api.characters.models import (
    Character
)

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id',
            'name',
            'species',
            'appearances',
        ]
