from django.db.models import Avg, Count
from rest_framework import serializers
from .models import Car, Rating


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.avg_rating


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rate', 'car']


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']

    def get_rates_number(self, rate):
        return rate.rates_number
