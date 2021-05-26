from django.urls import path
from apod import views

urlpatterns = [
    path('', views.apod, name='apod'),
]