from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def signup(request):
    return render(request, 'registration/signup.html')

