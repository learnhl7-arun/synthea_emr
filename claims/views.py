from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def claims (request):
	 return HttpResponse("Response from claims")
	 
