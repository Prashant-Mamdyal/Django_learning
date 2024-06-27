from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from learn_drf.models import Movie
from learn_drf.api.serializer import MovieSerializer


# @api_view()                                         #imported decorator to know which http method we are working on
# def movie_list(request):
#     movie = Movie.objects.all()
#     serializer = MovieSerializer(movie, many=True)      #remember to add 'many=true' if you returning data in list format
#     return Response(serializer.data)

# @api_view()
# def movie_details(request, pk):
#     movie = Movie.objects.get(id = pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)

#Implemented different methods like GET, POST, PUT, DELETE.
@api_view(['GET', 'POST'])                              
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serialier = MovieSerializer(movie, many=True)
        return Response(serialier.data)
    
    if request.method == 'POST':
        serialier = MovieSerializer(data=request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialier.errors)


@api_view(['GET','PUT','DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=pk)
        except:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(id = pk)
        movie.delete()
        return Response("Movie deleted successfully...", status = status.HTTP_204_NO_CONTENT)