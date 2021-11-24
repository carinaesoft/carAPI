from django.db.models import Avg, Count
from rest_framework import serializers
from .models import Car, Rating





class CarSerializer(serializers.ModelSerializer):

    avg_rating = serializers.SerializerMethodField()
    rates_number = serializers.SerializerMethodField()

    class Meta:

        model = Car
        fields = ['id','make', 'model', 'avg_rating', 'rates_number']

    def get_avg_rating(self, obj):
        return obj.rating.all().aggregate(Avg('rate'))['rate__avg']

    def get_rates_number(self, object):
        return object.rating.all().aggregate(Count('rate'))['rate__count']

class RateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Rating
        fields = ['rate', 'car']