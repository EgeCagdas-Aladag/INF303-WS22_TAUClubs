from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing accounts.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer 
    permission_classes = []