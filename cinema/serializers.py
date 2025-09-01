from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]

    def validate_duration(self, value):
        if value == 0:
            raise serializers.ValidationError("Duration must be greater than 0.")
        return value