from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from account.forms import *

# Create your views here.



class UserLoginView(LoginView):
	authentication_form = LoginForm
	template_name = 'account/login.html'


class UserLogoutView(LogoutView):
	next_page = reverse_lazy('login')
	


class UserRegistrationView(CreateView):
	form_class = RegistrationForm
	template_name = 'account/registration.html'
	success_url = reverse_lazy('login')




