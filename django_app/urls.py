from django .urls import path, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),  
    
    path('search/', SearchResultsView, name='search_results'),

    path('top_250/', Top_250View, name='top_250'),   
    path('action_movie/', ActionView, name='action_movie'), 
    path('comedy_movie/', ComedyView, name='comedy_movie'), 
    path('thriller_movie/', ThrillerView, name='thriller_movie'), 

    path('movie/new/', MovieCreateView.as_view(), name='movie_create'),      
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),  
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),  
    path('movies/', MovieListView2.as_view(), name='movie'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MovieListView.as_view(), name='home'),
    
    path('cartoon/<int:pk>/', CartoonDetailView.as_view(), name='cartoon_detail'),
    path('cartoon/new/', CartoonCreateView.as_view(), name='cartoon_create'),  
    path('cartoon/<int:pk>/update/', CartoonUpdateView.as_view(), name='cartoon_update'),  
    path('cartoon/<int:pk>/delete/', CartoonDeleteView.as_view(), name='cartoon_delete'),  
    path('cartoons/', CartoonListView.as_view(), name='cartoon'),
    
    path('profile/', ProfileView, name='profile'),

]
