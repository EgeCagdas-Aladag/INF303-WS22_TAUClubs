from django.db import models
from accounts import Manager
from accounts import Member

# Create your models here.

class Club(models.Model):
    name = models.CharField()
    manager = models.OneToOneField(Manager, on_delete=models.SET_NULL, blank=True, null=True) 
    members = models.ManyToManyField(Member, blank=True, null=True)
    responsibleLecturer = models.TextField()
    clubMail = models.EmailField()
