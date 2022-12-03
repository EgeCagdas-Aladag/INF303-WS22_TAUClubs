from django.db import models
from accounts.models import User

# from django.core.validators import MinLengthValidator

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=256)
    manager = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='+') 
    members = models.ManyToManyField(User, blank=True, null=True, related_name='+')
    responsibleLecturer = models.TextField()
    clubMail = models.EmailField()

class Post(models.Model):
    postId= models.CharField(max_length=256, primary_key=True)
    # name= models.CharField(validators=MinLengthValidator(2,"Name must be grater than 1 character"))
    name= models.CharField(max_length=256)
    postdate= models.DateField()
    clubname= models.ForeignKey('Club', on_delete=models.CASCADE, null=False)
    description= models.TextField(max_length=700)
    type= models.CharField(max_length=256)
