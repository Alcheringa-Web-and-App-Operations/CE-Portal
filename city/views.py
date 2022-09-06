from django.shortcuts import render

def landing(request) :
    return render(request, 'city/landing.html')

def dashboard(request) :
    return render(request, 'city/dashboard.html')

# Create your views here.
