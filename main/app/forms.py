from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User

# This piece of code creates a sign up form which can be used by a user in the 'templates/registration/login.html'
# which can be used to get POST data from user and then pass that data to the signup method in the 'views.py' file.
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=30, required=True)
    last_name = forms.CharField(label="Last Name", max_length=30, required=True)
    email = forms.EmailField(label="Email Address", widget=EmailInput, max_length=254)



    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", 'password1', 'password2')

class RatingForm(forms.Form):
    CHOICES = [('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),]

    rating = forms.ChoiceField(choices=CHOICES)
