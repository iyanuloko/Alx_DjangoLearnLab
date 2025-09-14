from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
