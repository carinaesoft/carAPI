from django.db.models import Count, Avg
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from .serializers import CarSerializer, RateSerializer, PopularSerializer
from .models import Car, Rating

from .vpic_check import check_car

'''@api_view(['GET', 'POST', 'DELETE'])
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
        result = check_car(request.data)

        #if car exists in vnic db
        if result == 'Found':
            car_serializer = CarSerializer(data = request.data)

            if car_serializer.is_valid():

                #check if car is in DB
                make = car_serializer.validated_data['make']
                model = car_serializer.validated_data['model']
                data_list = Car.objects.filter(make=make, model=model)
                if not data_list:
                    car_serializer.save()
                    return Response (car_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data={'message': 'Car already exists in database'},status=status.HTTP_400_BAD_REQUEST)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #if such make is not existing
        elif result == 'Empty response':
            info = f'Make is not existing {request.data}'
            return Response(info, status=status.HTTP_400_BAD_REQUEST)

        #if make exists but model not
        else:
            info = f'Model is not existing {request.data}'
            return Response(info, status=status.HTTP_400_BAD_REQUEST)
'''


class Cars(mixins.ListModelMixin,
           mixins.CreateModelMixin,
           generics.GenericAPIView,
           mixins.DestroyModelMixin):
    """

    Get list of cars, Post Car

    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        self.queryset = Car.objects.all().annotate(avg_rating=Avg('rates__rate'))
        return self.queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        result = check_car(request.data)
        serializer = CarSerializer(data=request.data)
        serializer.is_valid()
        try:
            make = serializer.validated_data['make']
            model = serializer.validated_data['model']
            data_list = Car.objects.filter(make=make, model=model)
            print(result)
            if serializer.is_valid():
                # if car is not in DB
                if not data_list:

                    # if car exists in vnic db
                    if result == "Found":
                        self.perform_create(serializer)
                        info = f'Car has been created {request.data} '
                        return Response({'success': info}, status=status.HTTP_201_CREATED)
                    else:
                        return Response(data={'message': 'Car already exists in database'},
                                        status=status.HTTP_400_BAD_REQUEST)

                # if such make is not existing
                elif result == 'Empty response':
                    info = f'Make is not existing {request.data}'
                    return Response({'error': info}, status=status.HTTP_400_BAD_REQUEST)

                # if make exists but model not
                else:
                    info = f'Model is not existing or is in DB {request.data}'
                    return Response({'error': info}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Wrong data in request'}, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Rating(mixins.ListModelMixin,
             mixins.CreateModelMixin,
             generics.GenericAPIView,
             mixins.DestroyModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Popular(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = PopularSerializer

    def get_queryset(self):
        self.queryset = Car.objects.all().annotate(rates_number=Count('rates')
                                                    ).order_by('-rates_number')
        return self.queryset