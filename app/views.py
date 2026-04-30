from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def get_home(request):
    return HttpResponse('Welcome to My blog')

def get_about(request):
    return HttpResponse("About Page")

def get_contact(request):
    return HttpResponse("<h1><b>Contact Page</b></h1>")