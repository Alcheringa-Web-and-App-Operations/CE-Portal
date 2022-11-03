import re
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
    data = request.POST
    form = PersonCreationForm()
    if City.objects.filter(id=cityVal).exists():
        availCity=City.objects.filter(id=cityVal).first().comingsoon
        if availCity:
            cityVal=0
    else:
        cityVal=0
    if request.method == 'POST':
        form = PersonCreationForm(data)
        if form.is_valid():
            email = request.POST['email']
            competition1 = request.POST.getlist('checkbox')
            city=request.POST['city']
            city = City.objects.get(id=city)
            competition = Competition.objects.filter(id__in=competition1).all()
            name = request.POST['name']
            countrycode = request.POST['countrycode']
            contactno=request.POST['contactno']
            college_name=request.POST['college_name']
            degree=request.POST['degree']
            gender=request.POST['gender']
            yearofgraduation=request.POST['yearofgraduation']
            for competition2 in competition:
                person = Person(name = name, email = email,city = city,competition = competition2,countrycode = countrycode,contactno = contactno,college_name = college_name,degree = degree,gender = gender,yearofgraduation = yearofgraduation)
                if(Person.objects.filter(email=email).filter(city=city).filter(competition=competition2)):
                    continue
                else:
                    person.save()
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

def teamForm(request):
    data = request.POST
    if request.method == 'POST':
        form = EntryFormTeams(request.POST)
        city = City.objects.filter(id = data.get('city')).first()
        competition = Competition.objects.filter(id = request.POST['checkbox']).first()
        members_email_list=[]
        for i in range( int(data.get('number'))):
            members_email_list.append((data.get('email' + str(i))))
        print(members_email_list)
        if not (len(members_email_list) == len(set(members_email_list))):
            messages.error(request,"Team Members should have unique Email-IDs")
        else:
            team = Team(name = data.get('name'),competition=competition,city=city)
            team.save()
            for i in range( int(data.get('number'))):
                if data.get('name' + str(i)) == "":
                    continue
                else:
                    
                    applicant = Person(name = data.get('name' + str(i)), email = data.get('email' + str(i)),city=city, countrycode = data.get('countryCode' + str(i)), contactno = data.get('phoneNo' + str(i)),college_name=data.get('collegename' + str(i)),gender=data.get('gender' + str(i)),yearofgraduation=data.get('year'+str(i)), solo = 0)
                    applicant.save()
                    team.members.add(applicant)
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
    return render(request, 'team/team.html',{'form': form})

def my_redirect(request):
    return redirect("https://alcheringa.in")

def cedetails(request):
    users_singles=Person.objects.all()
    users_team=Team.objects.all()
    return render(request, 'users/user_details.html',{'users_singles':users_singles,'users_team':users_team})