from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from verified_email_field.forms import VerifiedEmailField


class register_form(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['email']).exists():
            raise forms.ValidationError("This email is already taken !")
        return self.cleaned_data['username']

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match !")


class login_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
