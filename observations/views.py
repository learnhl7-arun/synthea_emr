from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def observations (request):
	 return HttpResponse("Response from observations")
	 
     