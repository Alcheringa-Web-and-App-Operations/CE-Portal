from django.shortcuts import render,redirect
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
        'range' : enumerate(city.cityCompetitions.all()),
        'compe':city.cityComp.all(),
        'cityVal':pk
    }
    if not city.cityCompetitions.all():
        return render(request, 'city/comingsoon.html',data)
    return render(request, 'city/dashboard.html',data)

def my_redirect(request):
    return redirect("https://alcheringa.in")

# Create your views here.
