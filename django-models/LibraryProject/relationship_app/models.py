from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Author(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def Meta

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
# Create your models here.
