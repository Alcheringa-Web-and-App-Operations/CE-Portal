from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.contrib import messages
=======

>>>>>>> master
from .forms import EntryForm, PersonCreationForm, EntryFormTeams
from .models import Competition, Person,City, Team
import json
from django.views.decorators.csrf import csrf_exempt


<<<<<<< HEAD
# print(email_lsist)
=======
>>>>>>> master
def register_single(request):
    data = request.POST

    form = PersonCreationForm()
<<<<<<< HEAD
    single = Person(pk = request.user.pk,name = data.get('name'))
=======
    # single = Person(name = data.get('name'))
>>>>>>> master
    # competitions =Person.competition
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            email_list = Person.objects.values_list('email',flat=True)
            email = request.POST['email']
            competition1 = request.POST['competition']
            competition = Competition.objects.get(id=competition1)
            # print(competition)
            # print(email)
            if (email in email_list):
                curr_user = Person.objects.filter(email=email).first()
                curr_user_comp = curr_user.competition.all()
                if (competition in curr_user_comp):
                    print("already registered, dont register again")
                    messages.error(request,f'Already registered for {competition}.')
                else:
                    print("merge it")
                    curr_user.competition.add(competition)
            else:
                form.save()
                return redirect('/')
=======
            form.save()
            return redirect('/')
>>>>>>> master

    # for comp in competitions:               
    #     single.competition.add(comp)
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
    data = request.POST
    if request.method == 'POST':
        form = EntryFormTeams(request.POST)
        
        city = City.objects.filter(id = data.get('city')).first()
        competition = Competition.objects.filter(id = data.get('competition')).first()
        team = Team(name = data.get('name'),competition=competition,city=city)
        team.save()
        team = Team.objects.all().last()
        for i in range( int(data.get('number'))):
            if data.get('name' + str(i)) == "":
                continue
            else:
                
                applicant = Person(name = data.get('name' + str(i)), email = data.get('email' + str(i)),city=city,contactno = data.get('phoneNo' + str(i)), solo = 0)
                querySet = Person.objects.filter(email = data.get('email' + str(i)))
                if querySet:
                    querySet.solo = 0
                else:
                    applicant.save()
                team.members.add(Person.objects.all().last().id)
        return redirect('/')    
        # person=get_object_or_404(Person)
        # if post.favourites.filter(id=request.user.id).exists():
        #     print()
        # else:
        #     post.favourites.add(request.user)
        # return HttpResponseRedirect(request.META['HTTP_REFERER'])
            

            # print(data)
    else:
        form = EntryFormTeams()
        return render(request, 'team/team.html',{'form': form})