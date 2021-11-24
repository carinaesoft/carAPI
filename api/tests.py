import json
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Car, Rating
from .serializers import CarSerializer, RateSerializer


test_car = {'make': 'Toyota', 'model':'Corona'}
test_no_model = {'make': 'Toyota', 'model':''}
test_wrong_car = {'make': 'Elon', 'model':'Musk'}
test_rate = {"car": "1", "rate": "3"}
test_higher_rate = {"car": "1", "rate": "44"}
class CarTestCase(APITestCase):

    def test_add_car(self):

        response = self.client.post("/api/cars/", test_car)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(Car.objects.get().model, 'Corona')

    def test_no_model(self):

        response = self.client.post("/api/cars/", test_no_model)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_cars(self):

        response = self.client.get("/api/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_car(self):
        response = self.client.post("/api/cars/", test_wrong_car)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RatingTestCase(APITestCase):

    def test_rate(self):
        self.client.post("/api/cars/", test_car)
        response = self.client.post("/api/rate/", test_rate )
        print(json.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)

    def test_higher_rate(self):
        self.client.post("/api/cars/", test_car)
        response = self.client.post("/api/rate/", test_higher_rate)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PopularTestCase(APITestCase):

    def test_popular(self):
        response = self.client.get("/api/popular/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)