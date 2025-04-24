from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from character.models import Character
from race.models import Race, SubRace
from race.serializers import RaceListSerializer, SubRaceSerializer


class RaceListView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceListSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubRaceListView(generics.ListAPIView):
    serializer_class = SubRaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return SubRace.objects.filter(race=pk)


class SubRaceChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "SubRaceChangeView"}, status=403)
        else:

            sub_race_id = request.data.get('id')
            change_sub_race = get_object_or_404(SubRace, id=sub_race_id)
            character.sub_race = change_sub_race
            character.save()
            return Response(SubRaceSerializer(character.sub_race, context={'character': character}).data)
