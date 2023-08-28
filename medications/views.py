from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def medications (request):
	 return HttpResponse("Response from medications")
	 

