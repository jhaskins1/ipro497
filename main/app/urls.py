from django.urls import path
from . import views

# This file acts as the URL mapper of the application.
# Suppose base URL for local environment is '127.0.0.1:8000'. If you add '/login' after the base URL, it
# should redirect to a login page that is prepared to receive user data.

# THIS urls.py FILE IS DIFFERENT FROM THE ONE IN main/urls.py. THIS FILE IS MORE ORIENTED TO THE APPLICATION
# RATHER THE DJANGO'S FRAMEWORK AND THE ADMIN SECTION. YOU WILL BE USING THIS FOR FILE FOR THE MOST PART.
urlpatterns = [
    path('', views.index, name='index'),
    # The code below suggests that if user adds '/login' after the base URL, the login_request function in
    # the views.py file will be called with the path name. The name of this URL mapper is 'login'.
    # If you observe the 'login_request' function in the views.py file, you should notice that it renders
    # a login.html page with instructions of what to do once user presses the submit button.
    path("login", views.login_request, name ="login"),
    # Similar implementation to that of login.
    path("logout", views.logout_request, name= "logout"),
    path('search', views.search, name="search"),
    path('show_movie/<movie_id>', views.show_movie, name="show-movie"),
]
