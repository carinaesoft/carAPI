from django.db import models

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rate = models.IntegerField()
    #avg_rating = models.Avg()
    rates_number = models.IntegerField()
