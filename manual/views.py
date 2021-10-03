from django.shortcuts import render
from django.views import generic

from manual.models import Post

class PostListView(generic.ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'manual/post_detail.html'