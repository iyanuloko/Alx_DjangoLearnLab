from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import SignUpForm
from django.http import request
from .models import UserProfile, Post, Comment, Tag
from django.db import models
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'blog/register.html'

class ProfileView(LoginRequiredMixin, CreateView):
    if request.method == 'POST':
        userpersona = UserProfile.objects.get(user=request.user)
        userpersona.email = models.EmailField()
        userpersona.profile_pic = models.ImageField(upload_to="profile_pic", null=True, blank=True)
        userpersona.save()

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

@login_required(login_url='login')
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

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/post_detail.html'

@login_required(login_url='login')
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/post_detail.html'
    fields = ['content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'blog/post_detail.html'
    fields = ['content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentUpdateView, self).form_valid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_detail.html'

def search_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
        tags = Post.objects.filter(tags__name__icontains=query)
        contents = Post.objects.filter(content__icontains=query)
    else:
        posts = Post.objects.all()
        tags = Tag.objects.all()
    return render(request, 'blog/post_search.html', {'posts': posts, 'tags': tags, 'contents': contents})