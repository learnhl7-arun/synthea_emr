from django.urls import path
from . import views

urlpatterns = [
    path('immunizations/', views.immunizations, name='immunizations'),
]