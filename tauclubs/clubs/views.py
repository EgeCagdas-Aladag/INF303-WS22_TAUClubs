from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tauclubs.permissions import IsClubManagerReadOn 
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Club, Post
from .serializers import ClubSerializer, PostSerializer
from rest_framework.filters import SearchFilter
from django.core.serializers import serialize

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
    def manager(self, request, pk=None):
        user = request.user
        club = self.get_object()
        club.pending_manager.add(user)

        return Response(status=201)

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        user = request.user
        club = self.get_object()
        club.followers.add(user)

        return Response(status=200)

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def admit_member(self, request, pk=None):
        club = self.get_object()
        if request.user == club.manager:

            data = request.data
            member = data["user"]
            
            club.members.add(member)
            club.pending_members.remove(member)

        return Response(status=201)

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
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsClubManagerReadOn]
    filter_backends= [SearchFilter]  
    search_fields=['clubname__id']  #search posts by id of the clubs by using /?search=id

    

    @action(detail=False, methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def get_followed_clubs_posts(self, request, pk=None):

        theclub = None 
        clubs = Club.objects.all() 
        queryset = Club.objects.none() 
        for i in clubs:
            print(clubs)
            if request.user in i.followers.all(): 
                
                queryset |= Club.objects.filter(pk=i.pk)
        
        list= []
        for a in queryset:
            list.append(a.id)
        queryset2=Post.objects.filter(clubname__pk__in=list)
        #queryset2 |= Post.objects.filter(pk=a.pk)
        qs_json = serialize('json', queryset=queryset2)
        return Response(data=qs_json , status=200)