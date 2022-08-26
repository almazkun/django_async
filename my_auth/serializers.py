from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "username"]

    def create(self, validated_data):
        return get_user_model().objects.create(**validated_data)
