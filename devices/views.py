from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def devices (request):
	 return HttpResponse("Response from devices")
	 
