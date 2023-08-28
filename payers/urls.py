from django.urls import path
from . import views

urlpatterns = [
    path('payers/', views.payers, name='payers'),
]