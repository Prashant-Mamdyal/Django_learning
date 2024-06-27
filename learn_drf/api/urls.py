from django.urls import path
#from learn_drf.api.views import movie_list, movie_details          #this urls for functions based views
from learn_drf.api.views import MovieList, MovieDetails

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetails.as_view(), name='movie-details'),
]