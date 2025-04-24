class CharacterProtectStateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer

    def patch(self, request, pk):
        # Получаем объект Character
        character = get_object_or_404(Character, pk=pk)
        # Проверяем права доступа
        if character.account != request.user:
            return Response({"error": "CharacterProtectStateView"}, status=403)
        # Получаем данные skill_state из запроса
        print(request.data)
        protect_state_data = request.data.get('protect_state', {})
        protect_state_id = protect_state_data.pop('id', None)
        try:
            # Обновляем существующий объект или создаем новый
            protect_state, created = ProtectStateModel.objects.update_or_create(
                id=protect_state_id,
                defaults=protect_state_data
            )
        except Exception as e:
            return Response({"error": f" {str(e)}"}, status=400)

        # Присваиваем объект character.skill_state
        character.protect_state = protect_state
        character.save()

        # Возвращаем сериализованные данные
        return Response(ProtectStateSerializer(protect_state).data)


class CharacterSkillStateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer

    def patch(self, request, pk):
        # Получаем объект Character
        character = get_object_or_404(Character, pk=pk)

        # Проверяем права доступа
        if character.account != request.user:
            return Response({"error": "CharacterSkillStateView"}, status=403)

        # Получаем данные skill_state из запроса
        skill_state_data = request.data.get('skill_state', {})
        skill_state_id = skill_state_data.pop('id', None)

        try:
            # Обновляем существующий объект или создаем новый
            skill_state, created = SkillStateModel.objects.update_or_create(
                id=skill_state_id,
                defaults=skill_state_data
            )
        except Exception as e:
            return Response({"error": f" {str(e)}"}, status=400)

        # Присваиваем объект character.skill_state
        character.skill_state = skill_state
        character.save()

        # Возвращаем сериализованные данные
        return Response(SkillStateSerializer(skill_state).data)


class CharacterSkillsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillsSerializer

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.skills:
            # Обновляем значения существующего объекта
            character.skills.strength = request.data.get('strength')
            character.skills.dexterity = request.data.get('dexterity')
            character.skills.constitution = request.data.get('constitution')
            character.skills.intelligence = request.data.get('intelligence')
            character.skills.wisdom = request.data.get('wisdom')
            character.skills.charisma = request.data.get('charisma')
            character.skills.save()
        return Response(SkillsSerializer(character.skills).data)


class CharacterDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer

    def delete(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CharacterDetailView(APIView):
    """Получение информации о персонаже."""

    def get(self, request, pk):
        try:
            character = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return Response({"error": "Character not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CharacterSerializer(character, context={'character': character})

        return Response(serializer.data)

    def patch(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        serializer = CharacterSerializer(character, context={'character': character}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializerList

    def get(self, request):
        queryset = Character.objects.filter(account=self.request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer_class = CreateCharacterSerializer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.save(account=self.request.user)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterCreateView(APIView):
    def post(self, request):
        serializer = CreateCharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(account=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
