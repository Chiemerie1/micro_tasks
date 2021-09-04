from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request=request, template_name="micro_tasks/homepage.html")

def log_in(request):
    signin_form = AuthenticationForm(request, data=request.POST)
    if request.method =="POST":
        signin_form =AuthenticationForm(request, data=request.POST)
        if signin_form.is_valid():
            username = signin_form.cleaned_data.get("username")
            password = signin_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return redirect("micro_tasks:console")
                messages.success(request, f"You are logged in as {username}")

    return render(request=request, template_name="micro_tasks/login.html",
                    context={"signin_form": signin_form})



def sign_up(request):
    signup_form = UserCreationForm(request.POST)
    if request.method == "POST":
        if signup_form.is_valid():
            new_user = signup_form.save()
            username = signup_form.cleaned_data.get("username")
            login(request, new_user)
            return redirect("micro_tasks:console")
            messages.success(request, f"Welcome {username}")

            
    return render(request=request, template_name="micro_tasks/sign_up.html",
                    context={"signup_form": signup_form})


def console(request):
    return render(request=request, template_name="micro_tasks/console.html")