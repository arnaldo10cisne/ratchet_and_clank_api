from rest_framework import viewsets
from rest_framework import permissions
from ratchet_and_clank_api.characters.models import (
    Character
)
from ratchet_and_clank_api.characters.serializers import (
    CharacterSerializer
)

# Create your views here.


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows characters to be viewed or edited.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]
