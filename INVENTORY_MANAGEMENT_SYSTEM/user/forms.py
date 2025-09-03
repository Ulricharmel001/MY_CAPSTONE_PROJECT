from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# -------------------
# Registration Form
# -------------------
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    profile_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password1", "password2", "date_of_birth", "profile_photo"]


# -------------------
# Login Form
# -------------------
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
