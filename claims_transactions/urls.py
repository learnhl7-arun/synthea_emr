from django.urls import path
from . import views

urlpatterns = [
    path('claims_transactions/', views.claims_transactions, name='claims_transactions'),
]