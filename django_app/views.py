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
from .form import MovieCreationForm
# Create your views here.
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
    

class CartoonListView(ListView):
    model = Cartoon
    template_name = 'cartoon.html'
    context_object_name = 'cartoons'
    
class CartoonDetailView(DetailView):
    model = Cartoon
    template_name = 'cartoon_detail.html'
    context_object_name = 'cartoon'
    
class CartoonCreateView(CreateView):
    model = Cartoon
    template_name = 'cartoon_create.html'
    fields = ['name', 'genre', 'country', 'duration', 'description', 'rating', 'manufacturing_date', 'image']
    
class CartoonUpdateView(UpdateView):
    model = Cartoon
    template_name = 'cartoon_update.html'
    fields = ['name', 'genre', 'country', 'duration', 'description', 'rating', 'manufacturing_date', 'image']
    
    
class CartoonDeleteView(DeleteView):
    model = Cartoon
    template_name = 'cartoon_delete.html'
    success_url = reverse_lazy('cartoon') 
    


def Top_250View(request):
    movies = Movie.objects.all()
    cartoons = Cartoon.objects.all()
    top_movies = []
    for movie in movies:
        top_movies.append(movie)
        
    for cartoon in cartoons:
        top_movies.append(cartoon)
                
        
    top_movies.sort(key=lambda x: -x.rating) # reverse=True
    return render(request=request, 
                  template_name="top_250.html",
                  context={
                      "top_movies": top_movies
                  })
    
def ActionView(request):
    movies = Movie.objects.all()
    cartoons = Cartoon.objects.all()
    action_movie = []
    
    for movie in movies:       
        if movie.genre.find('боевик') != -1:
            action_movie.append(movie)
     
            
        
    for cartoon in cartoons:
        if cartoon.genre.find('боевик') != -1:
            action_movie.append(cartoon)
    
            
    return render(request=request, 
                  template_name="action_movie.html",
                  context={
                      "action_movie": action_movie,
                  })
    
    
def ComedyView(request):
    movies = Movie.objects.all()
    cartoons = Cartoon.objects.all()
    comedy_movie = []
    
    for movie in movies:       
        if movie.genre.find('комедия') != -1:
            comedy_movie.append(movie)
     
            
        
    for cartoon in cartoons:
        if cartoon.genre.find('комедия') != -1:
            comedy_movie.append(cartoon)
                
    
    return render(request=request, 
                  template_name="comedy_movie.html",
                  context={
                      "comedy_movie": comedy_movie,
                  })
    
    
    
def ThrillerView(request):
    movies = Movie.objects.all()
    cartoons = Cartoon.objects.all()
    thriller_movie = []
    
    for movie in movies:       
        if movie.genre.find('триллер') != -1:
            thriller_movie.append(movie)
     
            
        
    for cartoon in cartoons:
        if cartoon.genre.find('триллер') != -1:
            thriller_movie.append(cartoon)
                
    
    return render(request, 
                  template_name="thriller_movie.html",
                  context={
                      "thriller_movie": thriller_movie,
                  })
    
    
# class SearchResultsView(ListView):
#     template_name = 'search_results.html'
#     movies = Movie.objects.all()
#     cartoons = Cartoon.objects.all()
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         search_movie = Movie.objects.filter(
#             Q(name__icontains=query)
#         )
#         return search_movie
    
    
def SearchResultsView(request):
    movies = Movie.objects.all()
    cartoons = Cartoon.objects.all()
    search_results = []
    movie_cartoon = []
    query = request.GET.get('q')
    for movie in movies:
        movie_cartoon.append(movie)
         
    for cartoon in cartoons:
        movie_cartoon.append(cartoon)
             
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
    return render(request=request, 
            template_name="profile.html",
            context={
                "user": request.user,
            })
    
    
    
    
    