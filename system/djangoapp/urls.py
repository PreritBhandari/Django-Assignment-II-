from django.contrib.auth.decorators import login_required

from .views import home, register_view, login_view, profile, logout_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),

    path('login/', login_view.as_view(), name='login'),
    path('profile/', login_required(profile.as_view()), name='profile'),
    path('logout/', logout_view.as_view(), name='logout'),

    path('register/', register_view.as_view(), name='register'),

]
