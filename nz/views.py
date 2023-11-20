from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kane (request):
    return HttpResponse('<h1>kane mama</h1>')

def ravindra (request):
    return HttpResponse('<h1>young star</h1>')