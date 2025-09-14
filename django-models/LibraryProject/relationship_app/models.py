from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
class Author(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        # this is a permissions tuple.
        permissions = (("can_add_book", "add book"), ("can_change_book", "change book"), ("can_delete_book", "delete book"))

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField()
    library = models.ManyToManyField(Library)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
        )
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
# Create your models here.
