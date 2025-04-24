from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from dnd.models import Character
from worldoutlook.models import WorldOutlook
from worldoutlook.serializers import WorldOutlookSerializer


class WorldOutlookView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorldOutlook.objects.all()
    serializer_class = WorldOutlookSerializer

    def get_queryset(self):
        return WorldOutlook.objects.all()

class CharacterWorldOutlookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, character_id):
        # Получаем персонажа по id
        character = get_object_or_404(Character, id=character_id)

        # Получаем ID мировоззрения из данных запроса
        world_outlook_id = request.data.get('id')
        if not world_outlook_id:
            return Response({'error': 'id is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        # Получаем объект предыстории
        world_outlook = get_object_or_404(WorldOutlook, id=world_outlook_id)
        # Привязываем предысторию к персонажу
        character.world_outlook = world_outlook
        character.save()
        # Возвращаем сериализованные данные персонажа
        serializer = WorldOutlookSerializer(character.world_outlook)
        return Response(serializer.data, status=status.HTTP_200_OK)
