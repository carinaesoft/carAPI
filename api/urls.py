from . import views, api_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
                #path('cars/' , api_views.cars),
                path('cars/' , api_views.Cars.as_view()),
                path('cars/<int:pk>/', api_views.CarDetail.as_view()),
                path('rate/', api_views.Rating.as_view()),
                path('popular/' , api_views.Popular.as_view()),
               ]
