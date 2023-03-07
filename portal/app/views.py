from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-post_datetime'
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detailed.html'
    context_object_name = 'post_det'