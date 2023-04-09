from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
