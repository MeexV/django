from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import RegistrForm
from django.views.generic import CreateView
from .models import ParsUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView):
    model = ParsUser
    template_name = 'usersapp/register.html'
    form_class = RegistrForm
    success_url = reverse_lazy('usersapp:login')


