from rest_framework import serializers
#from learn_drf.models import Movie
from learn_drf.models import WatchList, StreamPlatform, Review

# # Validators- created method for validating length of description
# def desc_length(value):
#     if len(value) > 20:
#         raise serializers.ValidationError("Description should be less then 10")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=20)
#     description = serializers.CharField(validators = [desc_length])
#     active = serializers.BooleanField()

#     # create method is for adding a new data to table. To implement a POST method we use a create method. 
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # update method is for updating a perticualar data/record in table. To implement a PUT method we use update method.
#     # we are updating old values with new values.
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     ### Validation in Serializer 
#     # there are 3 types - 1) Field-level validation - to validate a perticular field like name.
#     #                     2) Object-level validation - to validate multiple field like name and description.
#     #                     3) Validators - we add validator directly in serializer class for perticular field.

#     #Field-level Validation-
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Movie name is too short...")
#         return value
    
#     #Object-level Validation-
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should not be same")
#         return data

### implementing Model serializer 
# The ModelSerializer class is the same as a regular Serializer class, except that:

# It will automatically generate a set of fields for you, based on the model.
# It includes simple default implementations of .create() and .update().
# It won't add validation we have to add that.

# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()          #implementing serializer method field to create a custom field in serializer

#     class Meta:
#         model = Movie
#         fields = "__all__"
#         #fields = ['id', 'name', 'description']
#         #exclude = ['name']

#     def get_len_name(self, object):                        # we create method to calculate the length of name.
#         return len(object.name)                            # name of the method should be start from 'get_method_name'

#     #Field-level Validation-
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Movie name is too short...")
#         return value
    
#     #Object-level Validation-
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should not be same")
#         return data

### Updating new serializer class for new models
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only= True)

    class Meta:
        model = WatchList
        fields = "__all__"

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    # This is 'Nested Serializer' used to work with relationship. The Watchlist variable here is same as related_name in 'Watchlist' model
    watchlist = WatchListSerializer(many=True, read_only=True)      
                                                                    
    #if you want only title then it return whatever you define in __str__ method in models.
    #watchlist = serializers.StringRelatedField(many=True)

    #if you want primary key then it return movie primary key                           
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #if you want link of every movie to access it directly it will create a link      
    #watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-details')

    class Meta:
        model = StreamPlatform
        fields = "__all__"