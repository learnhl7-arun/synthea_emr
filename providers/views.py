from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def providers (request):
	 return HttpResponse("Response from providers")
	 
