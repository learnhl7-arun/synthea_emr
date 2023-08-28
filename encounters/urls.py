from django.urls import path
from . import views

urlpatterns = [
    path('encounters/', views.encounters, name='encounters'),
]