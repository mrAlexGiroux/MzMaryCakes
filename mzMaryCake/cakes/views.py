from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello, world! You're in the cake index.")

def cakeDetails(request, cake_name):
    return HttpResponse("You're looking at the cake %s." % cake_name)
