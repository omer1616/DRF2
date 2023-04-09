from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import  serializers
from django.contrib.auth.models import User
from ..models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PasswordSerializer(Serializer):
    password = serializers.CharField(max_length=128)