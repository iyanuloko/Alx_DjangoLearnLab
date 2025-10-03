from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from blog.models import Post, Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentForm(forms.ModelForm):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['author', 'content']

