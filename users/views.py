from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EntryForm, PersonCreationForm
from .models import Competition, Person,City, Team
import json
from django.views.decorators.csrf import csrf_exempt


def register_single(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'users/register_single.html', {'form': form})


# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change')
#     return render(request, 'users/home.html',{'form':form})
@csrf_exempt
def load_competitions(request):
    data=json.loads(request.body)
    competitions=City.objects.filter(id=data['city_id']).first().cityCompetitions.all()
    currentCompetition=""
    if data['current_competition']!="":
        currentCompetition=Competition.objects.filter(id=data['current_competition']).first()
    print(type(currentCompetition))
    return render(request,'users/city_dropdown_list_options.html',{"competitions":competitions,"competition_value":data['current_competition'],"currentCompetition":currentCompetition})

@csrf_exempt
def load_city(request):
    data=json.loads(request.body)
    cities=City.objects.filter(cityCompetitions__id=data['competition_id'])
    if data['current_city']!="":
        current_city=City.objects.filter(id=data['current_city']).first()
    else:
        current_city=""
    
    
    print(cities)
    return render(request,'users/comp_dropdown.html',{"cities":cities,"city_value":data['current_city'],"currentCity":current_city})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def teamForm(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        data = request.POST
        team = Team(name = data.get('name'))
        team.save()
        team = Team.objects.all().last()
        city = City.objects.filter(id = data.get('city')).first()
        competition = Competition.objects.filter(id = data.get('competition')).first()
        for i in range( int(data.get('number'))):
            applicant = Person(name = data.get('name' + str(i)), email = data.get('email' + str(i)), contactno = data.get('phoneNo' + str(i)), city = city, competition = competition, solo = 0)
            querySet = Person.objects.filter(email = data.get('email' + str(i)))
            if querySet:
                querySet.solo = 0
            else:
                applicant.save()
            team.members.add(Person.objects.all().last().id)
        print(data)
        return redirect('/')

    else:
        form = EntryForm()
        return render(request, 'team/team.html',{'form': form})