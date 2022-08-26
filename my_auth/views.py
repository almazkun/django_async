from django.contrib.auth import get_user_model
from rest_framework import viewsets

from my_auth.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
