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
        'compe':city.cityComp.all()
      
    }
    if not city.cityCompetitions.all():
        return render(request, 'city/comingsoon.html',data)
    elif(city.completionstatus==True):
        return render(request,'city/over.html',data)
    return render(request, 'city/dashboard.html',data)

def my_redirect(request):
    return redirect("https://alcheringa.in")

def sponsors(request):
    return render(request, 'city/sponsors.html')



# Create your views here.
