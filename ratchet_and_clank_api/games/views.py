from rest_framework import viewsets
from rest_framework import permissions
from ratchet_and_clank_api.games.models import (
    Game
)
from ratchet_and_clank_api.games.serializers import (
    GameSerializer
)

# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
