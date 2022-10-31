from django.shortcuts import render
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
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# def recommend(request):
#     api_key = "864e3baa97800ac0d0036fd1d008ca85"
#     movie_list = []
#     for id in range(550, 557):
#         url = "https://api.themoviedb.org/3/movie/" + id + "?api_key=" + api_key + "&language=en-US"
#         response = requests.get(url)
#         movie_list.append(response.json())

    



