from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, GroupSerializer, CharlistSerializer
from dnd.models import DndSpell, Character
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CharacterView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharlistSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        return Character.objects.filter(account = self.request.user)

    def create(self, request, *args, **kwargs):
        request.data.update({'account': request.user.id})
        return super(CharacterView, self).create(request, *args, **kwargs)



class SpellView(generics.ListAPIView):
    model = DndSpell
