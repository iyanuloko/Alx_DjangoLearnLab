from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'blog/register.html'

class ProfileView(CreateView):
    
# Create your views here.
