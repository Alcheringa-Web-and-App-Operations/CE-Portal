from django.shortcuts import render
from .models import City , Competition


def landing(request) :
    context = {
        'cities': City.objects.all(),
    }
    return render(request, 'city/landing.html',context)

def dashboard(request,pk) :
    city = City.objects.get(pk=pk)
<<<<<<< HEAD
=======
    
>>>>>>> master
    data = {
        'city' : city,
        'competitions': city.cityCompetitions.all(),
        'range' : enumerate(city.cityCompetitions.all()),
<<<<<<< HEAD
=======
        'compe':city.cityComp.all()
      

>>>>>>> master
    }
    return render(request, 'city/dashboard.html',data)

# Create your views here.
