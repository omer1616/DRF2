from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import UserSerializer, ProfileSerializer, PasswordSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsRequestUserPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, status
from ..models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import parsers
class ProfileViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsRequestUserPermission]

    @action(detail=False, methods=['get'])
    def user_count(self, request, pk=None):
        user_count = User.objects.all().count()
        return Response({'user_count': user_count})

    @action(detail=True, methods=['post'], serializer_class=PasswordSerializer)
    def set_password(self, request, pk=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance.set_password(serializer.validated_data['password'])
            instance.save()
            return Response({'status': 'password set'})
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
