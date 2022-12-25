from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def home(request):
 #   return render(request, 'home.html', {})

class home_View(ListView):
    model = Post
    template_name = 'home.html'

class detail_View(DetailView):
    model = Post 
    template_name = 'post_Detail.html'

class post_Add(CreateView):
    model = Post
    template_name ="post_Add.html"
    fields = ("__all__")


