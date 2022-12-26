from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import createForm

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
    form_class = createForm
    template_name ="post_Add.html"
    
    #dont need to use these anymore because I created a form class in forms.py
    #fields = ("__all__")

class update_View(UpdateView):
    model = Post
    template_name = 'post_Update.html'
    fields = ['title', 'body']
