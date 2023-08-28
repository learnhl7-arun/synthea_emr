from django.urls import path
from . import views

urlpatterns = [
    path('procedures/', views.procedures, name='procedures'),
]