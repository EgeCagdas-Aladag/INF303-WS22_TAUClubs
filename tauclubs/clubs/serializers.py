from rest_framework import serializers
from tauclubs.clubs.models import Club
from tauclubs.clubs.models import Post

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'manager', 'members', 'responsibleLecturer', 'clubMail']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postId','name','postdate','clubname','description','type']
