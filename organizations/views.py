from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def organizations (request):
	 return HttpResponse("Response from organizations")
	 