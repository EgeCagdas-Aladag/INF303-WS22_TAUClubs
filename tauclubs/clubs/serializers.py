from rest_framework import serializers
from tauclubs.clubs.models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'manager', 'members', 'responsibleLecturer', 'clubMail']
