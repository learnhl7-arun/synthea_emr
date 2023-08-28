from django.urls import path
from . import views

urlpatterns = [
    path('supplies/', views.supplies, name='supplies'),
]