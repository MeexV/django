from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token
from .forms import RegistrForm
from django.views.generic import CreateView, DetailView
from .models import ParsUser

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView):
    model = ParsUser
    template_name = 'usersapp/register.html'
    form_class = RegistrForm
    success_url = reverse_lazy('usersapp:login')

class UserDetailView(DetailView):
    template_name = 'usersapp/profile.html'
    model = ParsUser

def create_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    if not created:
        token.delete()
        token = Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))
