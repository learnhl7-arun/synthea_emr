from django.urls import path
from . import views

urlpatterns = [
    path('imaging_studies/', views.imaging_studies, name='imaging_studies'),
]