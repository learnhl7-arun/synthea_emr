from django.urls import path
from . import views

urlpatterns = [
    path('careplans/', views.careplans, name='careplans'),
]