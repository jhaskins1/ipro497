from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
import requests

def index(request):
    api_key = "864e3baa97800ac0d0036fd1d008ca85"
    movie_list = []
    for id in range(550, 557):
        url = "https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=" + api_key + "&language=en-US"
        response = requests.get(url)
        movie_list.append(response.json())
    return render(request, 'app/home.html', {'movie_list': movie_list})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})

# def recommend(request):
#     api_key = "864e3baa97800ac0d0036fd1d008ca85"
#     movie_list = []
#     for id in range(550, 557):
#         url = "https://api.themoviedb.org/3/movie/" + id + "?api_key=" + api_key + "&language=en-US"
#         response = requests.get(url)
#         movie_list.append(response.json())

    



