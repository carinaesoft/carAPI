from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Car(models.Model):
    # id = models.IntegerField(primary_key=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)


class Rating(models.Model):
    # id = models.IntegerField(primary_key=True)
    rate = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rating')



