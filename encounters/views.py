from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def encounters (request):
	 return HttpResponse("Response from encounters")
	 
