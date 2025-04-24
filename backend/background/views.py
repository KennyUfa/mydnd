from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from background.models import Background, SelectedOrigin, FeatureOption, Feature, SelectedFeatureOption, Flaw, Bond, Trait, Ideal
from background.serializers import BackgroundListSerializer, BackgroundSerializer, SelectedFeatureOptionSerializer, SelectedOriginSerializer
from dnd.models import Character


class BackgroundListView(generics.ListAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BackgroundChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.account != request.user:
            return Response({"error": "BackgroundChangeView"}, status=403)
        else:
            background_id = request.data.get('id')
            change = get_object_or_404(Background, id=background_id)

            if hasattr(character.background, 'id') and character.background.id != background_id:
                character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
                character_selected_origin_options.bond = None
                character_selected_origin_options.flaw = None
                character_selected_origin_options.ideal = None
                character_selected_origin_options.trait = None
                character_selected_origin_options.save()
            character.background = change
            character.save()
            return Response(BackgroundSerializer(character.background, context={'character': character}).data)


class BackgroundChangeOptionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        option = get_object_or_404(FeatureOption, id=request.data.get('option'))
        feature = get_object_or_404(Feature, id=request.data.get('feature'))
        existing_option = SelectedFeatureOption.objects.filter(character=character, feature=feature).first()
        if existing_option:
            # Обновляем существующую запись
            existing_option.option = option
            existing_option.save()
            return Response(SelectedFeatureOptionSerializer(existing_option).data)
        else:

            # Создаем новую запись

            res = SelectedFeatureOption.objects.create(
                character=character,
                feature=feature,
                option=option
            )
            return Response(SelectedFeatureOptionSerializer(res).data)


class BackgroundChangeOriginView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if request.data.get('flaw'):
            flaw = Flaw.objects.get(id=request.data.get('flaw').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.flaw = flaw
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('bond'):
            bond = Bond.objects.get(id=request.data.get('bond').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.bond = bond
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('trait'):
            trait = Trait.objects.get(id=request.data.get('trait').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.trait = trait
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
        if request.data.get('ideal'):
            ideal = Ideal.objects.get(id=request.data.get('ideal').get('id'))
            character_selected_origin_options, _ = SelectedOrigin.objects.get_or_create(character=character)
            character_selected_origin_options.ideal = ideal
            character_selected_origin_options.save()
            return Response(SelectedOriginSerializer(character_selected_origin_options).data)
