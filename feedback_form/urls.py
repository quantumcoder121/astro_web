from django.urls import path
from feedback_form import views

urlpatterns = [
    path('', views.response_form, name='response_form'),
    path('response_page/', views.response_page, name='response_page'),
]
