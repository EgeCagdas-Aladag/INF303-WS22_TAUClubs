from rest_framework import permissions
from pprint import pprint
from clubs.models import Club
from accounts.models import User

class IsClubManagerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

       theclub = None 
       clubs = Club.objects.all() 
       for i in range(0, len(clubs)):
            if clubs[i].manager == request.user:
                theclub = clubs[i].id
        
       if request.method in permissions.SAFE_METHODS:
            return True

       return theclub ==obj.clubname.id