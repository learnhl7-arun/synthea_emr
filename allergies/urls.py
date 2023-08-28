from django.urls import path
from . import views

urlpatterns = [
    path('allergies/', views.allergies, name='allergies'),
]