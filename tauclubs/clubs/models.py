from django.db import models
from accounts import Manager
from accounts import Member
from django.core.validators import MinLengthValidator

# Create your models here.

class Club(models.Model):
    name = models.CharField()
    manager = models.OneToOneField(Manager, on_delete=models.SET_NULL, blank=True, null=True) 
    members = models.ManyToManyField(Member, blank=True, null=True)
    responsibleLecturer = models.TextField()
    clubMail = models.EmailField()

class Post(models.Model):
    postId: models.CharField(primary_key=True)
    name: models.CharField(validators=MinLengthValidator(2,"Name must be grater than 1 character"))
    postdate: models.DateField()
    clubname: models.ForeignKey('Club', on_delete=models.CASCADE, null=False)
    description: models.TextField(max_length=700)
    type: models.CharField()
