from rest_framework import serializers
from learn_drf.models import Movie

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

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['name']

    #Field-level Validation-
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Movie name is too short...")
        return value
    
    #Object-level Validation-
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should not be same")
        return data