from django.shortcuts import render
from django.http import HttpResponse
from .models import Cake

def index(request):
        cake_list = Cake.object.order_by('-pub_date')[:5]
        output = ', '.join([q.cake_name for q in cake_list])
        return HttpResponse(output)

def cakeDetails(request, cake_name):
    return HttpResponse("You're looking at the cake %s." % cake_name)

def aboutMe(request):
        return HttpResponse("You're looking at who I am")
