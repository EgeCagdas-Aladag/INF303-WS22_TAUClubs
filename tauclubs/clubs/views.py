from django.shortcuts import render

from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated

from .models import Club
from .serializers import ClubSerializer


# Create your views here.
class ClubViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing clubs.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer 
    permission_classes = []

class PostViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing posts.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer 
    permission_classes = []