from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):
    return render(request=request, template_name="micro_tasks/homepage.html")