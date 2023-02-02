import time
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from dnd.models import *
from rest_framework import generics


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseClassChViewSet(generics.ListAPIView):
    queryset = BaseClassCh.objects.all()
    serializer_class = BaseClassChSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BaseClassCh.objects.all()


class RaceViewSet(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Race.objects.all()


class CharacterView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharlistSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        return Character.objects.filter(account=self.request.user)



class SpellView(viewsets.ReadOnlyModelViewSet):
    queryset = DndSpell.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    serializer_class = DndSpellBookSerializer
    search_fields = ['^name']

    # def list(self, request):
    #     serializer = DndSpellBookSerializer(self.queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = ChampionSpellSerializer(user)
        return Response(serializer.data)


class BackgroundView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BackgroundSerializer
    queryset = BackgroundModel.objects.all()


class ProtectStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProtectStateSerializer
    queryset = ProtectStateModel.objects.all()

class SkillStateView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SkillStateSerializer
    queryset = SkillStateModel.objects.all()




class PreHistoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PreHistoryModel.objects.all()
    serializer_class = PreHistorySerializer

    def get_queryset(self):
        # time.sleep(3)
        return PreHistoryModel.objects.all()

class WorldOutlookView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorldOutlook.objects.all()
    serializer_class = WorldOutlookSerializer

    def get_queryset(self):
        time.sleep(1)
        return WorldOutlook.objects.all()