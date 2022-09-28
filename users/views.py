from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EntryForm, PersonCreationForm, EntryFormTeams
from .models import Competition, Person,City, Team
import json
from django.views.decorators.csrf import csrf_exempt


# print(email_lsist)
def register_single(request):
    data = request.POST
    print(data)
    form = PersonCreationForm()
    single = Person(pk = request.user.pk,name = data.get('name'))
    # competitions =Person.competition
    if request.method == 'POST':
        print("here")
        form = PersonCreationForm(data)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            print("1234")
            email_list = Person.objects.values_list('email',flat=True)
            email = request.POST['email']
            # competition1 = Competition.objects.filter(id = request.POST['checkbox']).all()
            competition1 = request.POST.getlist('checkbox')
            print(competition1)
            competition = Competition.objects.filter(id__in=competition1).all()
            curr_user = Person.objects.filter(email=email).first()
            print(curr_user)
            for competition2 in competition:
                curr_user.competition.add(competition2)
                print(competition2)
            print(competition)
            # print(email)
            if (email in email_list):
                curr_user_comp = curr_user.competition.all()
                if (competition in curr_user_comp):
                    print("already registered, dont register again")
                    messages.error(request,f'Already registered for {competition}.')
                else:
                    print("merge it")
                    curr_user.competition.add(competition)
            else:
                print("fgdgf")
                form.save()
                return redirect('/')

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
    if data['city_id'] !="":
        competitions=City.objects.filter(id=data['city_id']).first().cityCompetitions.all()
        return render(request,'users/city_dropdown_list_options.html',{"competitions":competitions})
    else:
        return render(request,'users/city_dropdown_list_options.html')
        
    # currentCompetition=""
    # if data['current_competition']!="":
        # currentCompetition=Competition.objects.filter(id=data['current_competition']).first()
    # print(type(currentCompetition))
    # return render(request,'users/city_dropdown_list_options.html',{"competitions":competitions,"competition_value":data['current_competition'],"currentCompetition":currentCompetition})
    

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
    return JsonResponse(list(cities.values('id', 'name')), safe=False)

def teamForm(request):
    data = request.POST
    if request.method == 'POST':
        form = EntryFormTeams(request.POST)
        city = City.objects.filter(id = data.get('city')).first()
        competition = Competition.objects.filter(id = request.POST['checkbox']).first()
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