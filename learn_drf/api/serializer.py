from rest_framework import serializers
from learn_drf.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField()
    active = serializers.BooleanField()

    # create method is for adding a new data to table. To implement a POST method we use a create method. 
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # update method is for updating a perticualar data/record in table. To implement a PUT method we use update method.
    # we are updating old values with new values.
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance