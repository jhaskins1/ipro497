from django.shortcuts import render
from .forms import SignUpForm

def index(request):
    return render(request, 'app/home.html')

def signup(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

