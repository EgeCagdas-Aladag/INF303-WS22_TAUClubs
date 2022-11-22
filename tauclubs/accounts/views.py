from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer # Serializer not created yet
    permission_classes = []