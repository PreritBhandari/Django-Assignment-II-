from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'address', 'telephone_no', 'dob']
