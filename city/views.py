from django.shortcuts import render
from .models import City , Competition


def landing(request) :
    context = {
        'cities': City.objects.all(),
    }
    return render(request, 'city/landing.html',context)

def dashboard(request,pk) :
    city = City.objects.get(pk=pk)
    data = {
        'city' : city,
        'competitions': city.cityCompetitions.all(),
    }
    return render(request, 'city/dashboard.html',data)

# Create your views here.
