from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"})
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})
    )
    profile_photo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password1", "password2", "profile_photo"]


# Login form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
