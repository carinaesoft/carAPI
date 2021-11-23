from . import views, api_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
                path('cars/' , api_views.cars),
                path('rate/', api_views.rate)
               ]
