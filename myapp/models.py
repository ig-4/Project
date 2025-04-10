from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.CharField(max_length=300 , default="Travel")
    date = models.DateField()
    likes = models.ManyToManyField(User, related_name='liked_articles')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=300) 
    content = models.TextField()
    date_added = models.DateField()
    
    def __str__(self):
        return   '%s - %s' (self.article.title, self.name)

