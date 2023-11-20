from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohli(request):
    return HttpResponse('50 th odi century')

def iyer(request):
    return HttpResponse('back to back century')