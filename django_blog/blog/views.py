from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import SignUpForm
from django.http import request
from .models import UserProfile, Post
from django.db import models
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'blog/register.html'

class ProfileView(LoginRequiredMixin, CreateView):
    if request.method == 'POST':
        userpersona = UserProfile.objects.get(user=request.user)
        userpersona.email = models.EmailField()
        userpersona.profile_pic = models.ImageField(upload_to="profile_pic", null=True, blank=True)
        userpersona.save()

        return redirect('profile')

    return render(request, 'blog/profile.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author