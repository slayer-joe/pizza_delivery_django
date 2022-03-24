from django import forms
from django.contrib.auth import login, authenticate
from user.models import User
import time

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "password"}))

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        time.sleep(3)
        self.add_error('username', 'Invalid username')
        self.add_error('password', 'or invalid password')
        raise forms.ValidationError("User not found")

    def auth(self, request):
        login(request, self.user)
    

class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "password"}))

    class Meta:
        model = User
        fields = ["username", "phone", "email", "password"]
        widgets = {
            forms.PasswordInput(
                attrs={
                    "class": "input"
                }
            )
        }