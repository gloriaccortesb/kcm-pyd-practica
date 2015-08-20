from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import Post


class PostsView(ListView):
    model = Post
    template_name = 'blogs/posts_list.html'