"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from app import views as core_views


# This file acts as the URL mapper of the application.
# Suppose base URL for local environment is '127.0.0.1:8000'. If you add '/login' after the base URL, it
# should redirect to a login page that is prepared to receive user data.
urlpatterns = [
    path("admin/", admin.site.urls),
    # Adds all URL maps into this urls.py file.
    path('', include('app.urls')),
    # The code below suggests that if user adds '/login' after the base URL, the login_request function in
    # the views.py file will be called with the path name. The name of this URL mapper is 'login'.
    # If you observe the 'login_request' function in the views.py file, you should notice that it renders
    # a login.html page with instructions of what to do once user presses the submit button.
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', core_views.signup, name='signup'),
]
