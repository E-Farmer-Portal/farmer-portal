from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .forms import RegisterForm

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		form = RegisterForm()
		
	return render(response, "register/register.html", {"form":form})


def home(response):
    return render(response, "register/home.html")
