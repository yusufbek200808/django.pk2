from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignInForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Enter your username')
    username = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Enter password')

    class Meta:
        model = User
        fields = ['username', 'password']


class SignUpForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Create any username')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Enter password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']