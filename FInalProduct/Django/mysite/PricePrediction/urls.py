from django.contrib import admin
from django.urls import path
from PricePrediction import views


urlpatterns = [
    path("", views.homePage, name="homePage"),
    path('prediction/', views.predictionForm, name='predictionForm'),
]