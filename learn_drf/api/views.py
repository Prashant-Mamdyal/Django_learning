from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

#from learn_drf.models import Movie
from learn_drf.models import WatchList, StreamPlatform, Review
#from learn_drf.api.serializer import MovieSerializer
from learn_drf.api.serializer import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


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


### Implemented different methods like GET, POST, PUT, DELETE.

# @api_view(['GET', 'POST'])                              
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serialier = MovieSerializer(movie, many=True)
#         return Response(serialier.data)
    
#     if request.method == 'POST':
#         serialier = MovieSerializer(data=request.data)
#         if serialier.is_valid():
#             serialier.save()
#             return Response(serialier.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialier.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(id=pk)
#         except:
#             return Response({"error": "Movie not present"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(id=pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(id = pk)
#         movie.delete()
#         return Response("Movie deleted successfully...", status = status.HTTP_204_NO_CONTENT)


### Implementing Class based views

# class MovieList(APIView):
#
#     def get(self, request):
#         movie = Movie.objects.all()
#         serialier = MovieSerializer(movie, many=True)
#         return Response(serialier.data)
    
#     def post(self, request):
#         serialier = MovieSerializer(data=request.data)
#         if serialier.is_valid():
#             serialier.save()
#             return Response(serialier.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialier.errors)
        

# class MovieDetails(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(id = pk)
#         except:
#             return Response({"error": "Movie not present"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         movie = Movie.objects.get(id = pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, pk):
#         movie = Movie.objects.get(id = pk)
#         movie.delete()
#         return Response("Movie deleted Successfully...", status=status.HTTP_204_NO_CONTENT)


### Creating views for watchlist models
class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetails(APIView):
    def get(self, request, pk):
        try:
            watchdetail = WatchList.objects.get(id = pk)
        except:
            return Response({"error":"Movie not present"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(watchdetail)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchdetail = WatchList.objects.get(id = pk)
        serializer = WatchListSerializer(watchdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        watchdetail = WatchList.objects.get(id = pk)
        watchdetail.delete()
        return Response("Deleted successfully...", status=status.HTTP_204_NO_CONTENT)
    
#creating views for streamplatform models
class StreamPlatformListAV(APIView):
    def get(self, request):
        stream = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream, many = True) #context={'request': request} is added as third parameter here when you want to work with HyperlinkedRelatedField in serializer.
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class StreamPlatformDetails(APIView):
    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(id = pk)
        except:
            return Response({"error":"item not present"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    def put(self, request, pk):
        stream = StreamPlatform.objects.get(id = pk)
        serializer = StreamPlatformSerializer(stream, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(id = pk)
        stream.delete()
        return Response("item is deleted...", status=status.HTTP_204_NO_CONTENT)
    

#creating class based views using Mixins
class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)
    
class ReviewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
