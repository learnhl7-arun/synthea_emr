from django.urls import path
from . import views

urlpatterns = [
    path('observations/', views.observations, name='observations'),
]