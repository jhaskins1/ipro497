from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

def index(request):
    return HttpResponse("Hello world!")

def signup(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

