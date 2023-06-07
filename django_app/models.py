from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    genre = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    duration = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.FloatField(null=False, blank=False)
    manufacturing_date = models.PositiveIntegerField(null=False, blank=False)
    image = models.ImageField(default="default.jpg", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})
  

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.movie.name, self.name)
    
    def get_absolute_url(self):
        return reverse("movie")
  
    

class Klient(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return str(self.name)
    
    



    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    

