from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def allergies (request):
	 return HttpResponse("Response from allergies")

