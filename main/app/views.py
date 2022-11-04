from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from .forms import SignUpForm
import requests
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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

    
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request, 'app/home.html')



