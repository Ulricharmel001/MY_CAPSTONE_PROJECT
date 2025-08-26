from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Registration Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name", "password1", "password2", "date_of_birth", "profile_photo"]

# Login Form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # login with email
