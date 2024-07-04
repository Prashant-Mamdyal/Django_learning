from django.contrib import admin
#from learn_drf.models import Movie
from learn_drf.models import WatchList, StreamPlatform, Review


# Register your models here.
#admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
