from django.db import models
from django.urls import reverse
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
        return reverse("movie")
  
class Cartoon(models.Model):
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
        return reverse("cartoon", args=[str(self.id)])
    
class Top_250(models.Model):
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



    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    

