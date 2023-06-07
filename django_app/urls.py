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
    path('multfilm_movie/', MultfilmView, name='multfilm_movie'), 

    path('movie/new/', MovieCreateView.as_view(), name='movie_create'),      
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),  
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),  
    path('movies/', MovieListView2.as_view(), name='movie'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', MovieListView.as_view(), name='home'),
    
    path('profile/', ProfileView, name='profile'),
    path('movie/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
]
