from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request=request, template_name="micro_tasks/homepage.html")

def login(request):
    return render(request=request, template_name="micro_tasks/login.html")



def sign_up(request):
    signup_form = UserCreationForm(request.POST)
    if request.method == "POST":
        if signup_form.is_valid():
            new_user = signup_form.save()
            username = signup_form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}")
            
        
    signup_form = UserCreationForm
    return render(request=request, template_name="micro_tasks/sign_up.html",
                    context={"signup_form": signup_form})