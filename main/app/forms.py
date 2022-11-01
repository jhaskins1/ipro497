from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    f_name = forms.CharField(label="First Name", max_length=30, required=True)
    l_name = forms.CharField(label="Last Name", max_length=30, required=True)
    email = forms.EmailField(label="Email Address", widget=EmailInput, max_length=254)

    class Meta:
        model = User
        fields = ("f_name", "l_name", "username", "email",)
