from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):
    return render(request=request, template_name="micro_tasks/homepage.html")

def login(request):
    return render(request=request, template_name="micro_tasks/login.html")

def sign_up(request):
    return render(request=request, template_name="micro_tasks/sign_up.html")