# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):
    # Fields from the User model
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
    )
    
    # Fields from the UserProfile model
    bio = forms.CharField(max_length=500, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'image']
