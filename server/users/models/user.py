from django.db.models import *
from django.contrib.auth.models import AbstractUser
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class User(AbstractUser):
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=24)

    def __str__(self):
        return self.username

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']

class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
