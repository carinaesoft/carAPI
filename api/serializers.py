from django.db.models import Avg
from rest_framework import serializers
from .models import Car, Rating





class CarSerializer(serializers.ModelSerializer):

    avg_rating = serializers.SerializerMethodField()

    class Meta:

        model = Car
        fields = ['id','make', 'model', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating.all().aggregate(Avg('rate'))
class RateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Rating
        fields = ['rate', 'car']