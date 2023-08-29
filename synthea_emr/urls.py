"""
URL configuration for synthea_emr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('allergies.urls')),
    path('', include('careplans.urls')),
    path('', include('claims.urls')),
    path('', include('claims_transactions.urls')),
    path('', include('conditions.urls')),
    path('', include('devices.urls')),
    path('', include('encounters.urls')),
    path('', include('imaging_studies.urls')),
    path('', include('immunizations.urls')),
    path('', include('medications.urls')),
    path('', include('observations.urls')),
    path('', include('organizations.urls')),
    path('', include('patients.urls')),
    path('', include('payers.urls')),
    path('', include('procedures.urls')),
    path('', include('providers.urls')),
    path('', include('supplies.urls')),
    path('admin/', admin.site.urls),
]
