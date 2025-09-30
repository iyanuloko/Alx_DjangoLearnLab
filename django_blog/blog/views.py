from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import SignUpForm
from django.http import request
from .models import UserProfile
from django.db import models
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'blog/register.html'

if request.method == 'POST':
    userpersona = UserProfile.objects.get(user=request.user)
    userpersona.email = models.EmailField()
    userpersona.profile_pic = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    userpersona.save()

    return redirect('profile')

return render(request, 'blog/profile.html')

