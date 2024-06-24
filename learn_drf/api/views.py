from rest_framework.response import Response
from rest_framework.decorators import api_view

from learn_drf.models import Movie
from learn_drf.api.serializer import MovieSerializer


@api_view()                                         #imported decorator to know which http method we are working on
def movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)      #remember to add 'many=true' if you returning data in list format
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(id = pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)