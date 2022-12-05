from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Club, Post
from .serializers import ClubSerializer, PostSerializer


# Create your views here.
class ClubViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing clubs.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer 
    permission_classes = []

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def membership(self, request, pk=None):
        user = request.user
        club = self.get_object()
        club.pending_members.add(user)

        return Response(status=201)

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user = request.user
        club = self.get_object()
        club.followers.add(user)

        return Response(status=200)

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        user = request.user
        club = self.get_object()
        club.followers.remove(user)

        return Response(status=200)

class PostViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for viewing and editing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []