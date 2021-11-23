from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import Car, Rating
from .serializers import CarSerializer, RateSerializer



@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def rate(request):

    if request.method == 'GET':
        rate = Rating.objects.all()
        rate_serializer = RateSerializer(rate, many = True)
        return Response(rate_serializer.data)
    elif request.method == "POST":
        rate_serializer = RateSerializer(data = request.data)
        if rate_serializer.is_valid():
            rate_serializer.save()
            return Response (rate_serializer.data, status=status.HTTP_201_CREATED)
        return Response(rate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars, many = True)
        return Response(car_serializer.data)
    elif request.method == 'POST':
        if
        car_serializer = CarSerializer(data = request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response (car_serializer.data, status=status.HTTP_201_CREATED)
        return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)