from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from learn_drf.api.views import movie_list, movie_details          #this urls for functions based views
#from learn_drf.api.views import MovieList, MovieDetails
from learn_drf.api.views import WatchListAV, WatchDetails, StreamPlatformListAV, StreamPlatformDetails, ReviewCreate, ReviewList, ReviewDetails, StreamPlatform_VS

router = DefaultRouter()
router.register('stream', StreamPlatform_VS, basename='streamplatform')

urlpatterns = [
    # path('list/', MovieList.as_view(), name='movie-list'),
    # path('<int:pk>', MovieDetails.as_view(), name='movie-details'),

    path('watch/list/', WatchListAV.as_view(), name = 'watch-list'),
    path('watch/<int:pk>', WatchDetails.as_view(), name = 'watch-details'),

    path('', include(router.urls)),
    # for both this urls we implemented a router 
    
    # path('stream/list/', StreamPlatformListAV.as_view(), name = 'streamplatform-list'),
    # path('stream/<int:pk>', StreamPlatformDetails.as_view(), name = 'streamplatform-details'),

    # path('review/list/', ReviewList.as_view(), name ='review-list'),                  # here we are getting list of review
    # path('review/<int:pk>', ReviewDetails.as_view(), name = 'review-deatils'),        # here we are getting perticular review

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'review-create'),# here we are adding new review for selected movie id
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'review-list'),         # updating urls, so we get all reviews for perticular movie id
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name = 'review-details')    # here we are getting perticular review using review id
]       