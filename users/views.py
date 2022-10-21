from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EntryForm, PersonCreationForm, EntryFormTeams
from .models import Competition, Person,City, Team
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# print(email_list)
def register_single(request,cityVal=0):
    # if len(str(request.META.get('HTTP_REFERER')).split("dashboard/"))>1:
    #     cityVal=(request.META.get('HTTP_REFERER')).split("dashboard/")[1]
    data = request.POST
    form = PersonCreationForm()
    single = Person(pk = request.user.pk,name = data.get('name'))
    if City.objects.filter(id=cityVal).exists():
        availCity=City.objects.filter(id=cityVal).first().comingsoon
        if availCity:
            cityVal=0
    else:
        cityVal=0
    if request.method == 'POST':
        form = PersonCreationForm(data)
        if form.is_valid():
            email_list = Person.objects.values_list('email',flat=True)
            email = request.POST['email']
            competition1 = request.POST.getlist('checkbox')
            city=request.POST['city']
            print(city)
            competition = Competition.objects.filter(id__in=competition1).all()
            if Person.objects.filter(email=email):
                curr_user = Person.objects.filter(email=email).first()
                for competition2 in competition:
                    curr_user.competition.add(competition2)
                if (email in email_list):
                    curr_user_comp = curr_user.competition.all()
                    if (competition2 in curr_user_comp):
                        # print("already registered, dont register again")
                        messages.error(request,f'Already registered for these competitions.')
                    else:
                        # print("merge it")
                        curr_user.competition.add(competition2)
            else:
                form.save()
                curr_user = Person.objects.filter(email=email).first()
                curr_user.gender = request.POST['gender']
                curr_user.degree = request.POST['degree']
                for competition2 in competition:
                    curr_user.competition.add(competition2)
                curr_user.save()
                return redirect('success')

    # for comp in competitions:               
    #     single.competition.add(comp)
    return render(request, 'users/register_single.html', {'form': form,"cityVal":cityVal})


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
def load_competitions_single(request):
    data=json.loads(request.body)
    if data['city_id'] !="":
        competitions=City.objects.filter(id=data['city_id']).first().cityCompetitions.all()
        competitions1 = competitions.filter(minimum_user=1).all()
        return render(request,'users/city_dropdown_list_options.html',{"competitions":competitions1})
    else:
        return render(request,'users/city_dropdown_list_options.html')


@csrf_exempt
def load_competitions_team(request):
    data=json.loads(request.body)
    if data['city_id'] !="":
        competitions=City.objects.filter(id=data['city_id']).first().cityCompetitions.all()
        competitions1 = competitions.filter(minimum_user__gte=2)
        return render(request,'users/city_dropdown_list_options.html',{"competitions":competitions1})
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

@csrf_exempt
def load_minmax(request):
    data=json.loads(request.body)
    comp=Competition.objects.filter(id=data['comp_id']).first()
    return JsonResponse({"minuser":comp.minimum_user,"maxuser":comp.maximum_user})

def success(request):
    return render(request, 'users/success.html')

def teamForm(request,cityVal=0):
    data = request.POST
    if City.objects.filter(id=cityVal).exists():
        availCity=City.objects.filter(id=cityVal).first().comingsoon
        if availCity:
            cityVal=0
    else:
        cityVal=0
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
                
                applicant = Person(name = data.get('name' + str(i)), email = data.get('email' + str(i)),city=city, countrycode = data.get('countryCode' + str(i)), contactno = data.get('phoneNo' + str(i)),college_name=data.get('collegename' + str(i)),gender=data.get('gender' + str(i)),yearofgraduation=data.get('year'+str(i)), solo = 0)
                querySet = Person.objects.filter(email = data.get('email' + str(i)))
                if querySet:
                    querySet.solo = 0
                else:
                    applicant.save()
                team.members.add(Person.objects.all().last().id)
        return redirect('success')    
        # person=get_object_or_404(Person)
        # if post.favourites.filter(id=request.user.id).exists():
        #     print()
        # else:
        #     post.favourites.add(request.user)
        # return HttpResponseRedirect(request.META['HTTP_REFERER'])
            

            # print(data)
    else:
        form = EntryFormTeams()
        return render(request, 'team/team.html',{'form': form,"cityVal":cityVal})

def my_redirect(request):
    return redirect("https://alcheringa.in")

def cedetails(request):
    users_singles=Person.objects.all()
    users_team=Team.objects.all()
    return render(request, 'users/user_details.html',{'users_singles':users_singles,'users_team':users_team})