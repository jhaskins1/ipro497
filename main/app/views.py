from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from .forms import SignUpForm
import requests
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# This file is used for storing functions of logic and processing of information. 
# E.g. if a user signs up on the sign-up form, this file stores the code of the implementation of the sign-up authentication
# to store user credentials into the application's database.


# This function fetches the movie_details of movies with movie_id from 550 to 556 as a sample/demo for displaying random information
# on the application's homepage. This also checks if API works or not. 
def index(request):
    api_key = "864e3baa97800ac0d0036fd1d008ca85"
    movie_list = []
    for id in range(550, 557):
        url = "https://api.themoviedb.org/3/movie/" + str(id) + "?api_key=" + api_key + "&language=en-US"
        response = requests.get(url)
        movie_list.append(response.json())
    return render(request, 'app/home.html', {'movie_list': movie_list})


# This function/code receives the data the user inputs in the sign-up form and then stores the POST data into the SQLite3 database.
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

# This function/code receives the data the user inputs in the login authentication form and then checks
# if the credentials match the existing user records in the database.
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'registration/login.html', {'form':form})



# This piece of code 'de-authenticates' the user from the application.   
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request, 'app/home.html')


def search(request):
    #Query the database hear
    return render(request, 'app/search.html', {})

