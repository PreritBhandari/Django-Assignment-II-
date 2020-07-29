from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from django.views.generic import CreateView, FormView

from .forms import register_form, login_form

from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, 'djangoapp/home.html')


class register_view(FormView):
    def post(self, request, *args, **kwargs):
        form = register_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = User(
                username=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            user.set_password(form.cleaned_data['password'])  ## hash ko ma password display garna ko lagi
            user.save()

            email = form.cleaned_data['email']
            subject = f'Your Account is verified as {email}'
            message = f'Congratulations!! Your account is verified as {email} and now you can access our site as our User.Thank You!'
            from_email = 'admin@admin.com'
            recipients = [request.user.username, ]
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipients)
            print(f'verification sent to {email}')
            return redirect('login')
        return redirect('register')

    def get(self, request, *args, **kwargs):
        form = register_form()
        return render(request, 'djangoapp/register.html', {'form': form})


class login_view(View):
    # form_class = AuthenticationForm
    #
    template_name = 'djangoapp/login.html'

    # success_url = 'profile'

    def post(self, request, *args, **kwargs):
        form = login_form(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user:
                print('user found', user)
                login(request, user)
                return redirect('profile-create')
            else:
                print('user not found', user)
        return redirect('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile-create')

        form = login_form()
        return render(request, 'djangoapp/login.html', {'form': form})


class profile(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'djangoapp/profile.html')


class logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('login')
