from django.urls import path
from . import views

urlpatterns = [
    path('claims/', views.claims, name='claims'),
]