from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.template import loader, Context
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def inicio(request):
	
	return render(request, "index.html")


