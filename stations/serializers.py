from rest_framework import serializers
from stations.models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('name', 'neighbors', 'arrival_popularity', 'departure_popularity')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Station.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.title)
        instance.code = validated_data.get('neighbors', instance.code)
        instance.linenos = validated_data.get('arrival_popularity', instance.linenos)
        instance.language = validated_data.get('departure_popularity', instance.language)        
        instance.save()
        return instance
