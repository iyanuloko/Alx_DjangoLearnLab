from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    REQUIRED_FIELDS = ['email']

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, profile_photo=None, phone_number=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, profile_photo=profile_photo, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
# Create your models here.
