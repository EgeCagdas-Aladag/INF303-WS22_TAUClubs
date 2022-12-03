from rest_framework import serializers
from .models import Club
from .models import Post

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'manager', 'members', 'pending_members','responsibleLecturer', 'clubMail', 'followers']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postId','name','postdate','clubname','description','type']
