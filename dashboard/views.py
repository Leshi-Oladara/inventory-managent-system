from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("this is the homepage")

def employees(request):
    return HttpResponse("This is the employee page")