from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, is_staff = False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        email = self.normalize_email(email)
        user = self.model(email = email)

        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password: str) -> "User":
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            is_staff = True,
            is_superuser = True
        )

        user.save()

        return user
       

class User(AbstractUser):
    username = None
    first_name = models.CharField(verbose_name="First Name", max_length=255, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, null=False)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()