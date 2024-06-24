# from learn_drf.models import Movie
# from django.http import JsonResponse

# # Creating basic views and returning data using Jsonresponse.
# def movie_list(request):
#     movie = Movie.objects.all()             #accessing the whole movie list
#     data = {
#         'movie':list(movie.values())        #here converting complex queryset data into python dictionary using values() method 
#     }                                       #and then converting python dictionary into json format using Jsonresponse                                              
#     return JsonResponse(data)

# def movie_details(request, pk):             #accesssing perticular movie details using id
#     movie = Movie.objects.get(id = pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'status': movie.active
#     }
#     return JsonResponse(data)