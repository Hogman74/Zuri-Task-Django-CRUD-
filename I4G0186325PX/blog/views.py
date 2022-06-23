from audioop import reverse
from dataclasses import field
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
      
    
class PostCreateView(CreateView):
    model = Post
    field = "_all_"
    success_url = reverse_lazy("blog:all")
    

class PostDetailView(DetailView):
    model = Post
   

class PostUpdateView(UpdateView):
    model = Post
    field = "_all_"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = Post
    field = "_all_"
    success_url = reverse_lazy("blog:all")    
     