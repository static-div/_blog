from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
# used to convert an object of a model into a string representation. This method is called when you use the str() function on an object of a model, or when you print an object of a model.
    def __str__(self):
        return 'Author:' + self.title + '-' + str(self.author)

#this allows user to post, redirect to created post
    def get_absolute_url(self):
       # return reverse('post_Detail', args=(str(self.id)) )
       return reverse('home')
