from django.shortcuts import render
from django.views.generic import \
    ListView, \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registarion.html'
class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'movies'
    
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    
class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movie_create.html'
    fields = ['name', 'genre', 'country', 'duration', 'description', 'rating', 'manufacturing_date', 'image']
    
    
class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie_update.html'
    fields = ['name', 'genre', 'country', 'duration', 'description', 'rating', 'manufacturing_date', 'image']
    
    
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('movie') 
    
class MovieListView2(ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movies'
    


def Top_250View(request):
    movies = Movie.objects.all()
    top_movies = []
    for movie in movies:
        top_movies.append(movie)
                
        
    top_movies.sort(key=lambda x: -x.rating) # reverse=True
    return render(request=request, 
                  template_name="top_250.html",
                  context={
                      "top_movies": top_movies
                  })
    
def ActionView(request):
    movies = Movie.objects.all()
    action_movie = []
    
    for movie in movies:       
        if movie.genre.find('боевик') != -1:
            action_movie.append(movie)
     
    return render(request=request, 
                  template_name="action_movie.html",
                  context={
                      "action_movie": action_movie,
                  })
    
    
def ComedyView(request):
    movies = Movie.objects.all()
    comedy_movie = []
    
    for movie in movies:       
        if movie.genre.find('комедия') != -1:
            comedy_movie.append(movie)
     
    
    return render(request=request, 
                  template_name="comedy_movie.html",
                  context={
                      "comedy_movie": comedy_movie,
                  })
    
    
    
def ThrillerView(request):
    movies = Movie.objects.all()
    thriller_movie = []
    
    for movie in movies:       
        if movie.genre.find('триллер') != -1:
            thriller_movie.append(movie)
     
    
    return render(request, 
                  template_name="thriller_movie.html",
                  context={
                      "thriller_movie": thriller_movie,
                  })
    
def MultfilmView(request):
    movies = Movie.objects.all()
    multfilm = []
    for movie in movies:       
        if movie.genre.find('мультфильм') != -1:
            multfilm.append(movie)

    return render(request, 
                  template_name="multfilm_movie.html",
                  context={
                      "multfilm": multfilm,
                  })
    

    
def SearchResultsView(request):
    movies = Movie.objects.all()
    search_results = []
    movie_cartoon = []
    query = request.GET.get('q')
    for movie in movies:
        movie_cartoon.append(movie)

    for movie in movie_cartoon:
        if str(movie.name).find(query) != -1:    
            search_results.append(movie)
            
            
    if len(search_results) == 1:
        return render(request=request, 
        template_name="search_results.html",
        context={
            "movie": search_results[0],
        })
    elif len(search_results) > 1:
        return render(request=request, 
        template_name="movie.html",
        context={
            "movies": search_results,
        })
            
    return render(request,
                  template_name='notfound.html')


def ProfileView(request):
    klient = Klient.objects.get(name=request.user)
    return render(request=request, 
            template_name="profile.html",
            context={
                "klient": klient
            })
    
    
    
    
class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'
    
    