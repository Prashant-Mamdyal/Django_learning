from django.urls import path
#from learn_drf.api.views import movie_list, movie_details          #this urls for functions based views
#from learn_drf.api.views import MovieList, MovieDetails
from learn_drf.api.views import WatchListAV, WatchDetails, StreamPlatformListAV, StreamPlatformDetails, ReviewList, ReviewDetails

urlpatterns = [
    # path('list/', MovieList.as_view(), name='movie-list'),
    # path('<int:pk>', MovieDetails.as_view(), name='movie-details'),

    path('watch/list/', WatchListAV.as_view(), name = 'watch-list'),
    path('watch/<int:pk>', WatchDetails.as_view(), name = 'watch-details'),

    path('stream/list/', StreamPlatformListAV.as_view(), name = 'streamplatform-list'),
    path('stream/<int:pk>', StreamPlatformDetails.as_view(), name = 'streamplatform-details'),

    path('review/list/', ReviewList.as_view(), name ='review-list'),
    path('review/<int:pk>', ReviewDetails.as_view(), name = 'review-deatils'),
]       