from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Competition, Person


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'users/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change')
    return render(request, 'users/home.html',{'form':form})


# AJAX
def load_competitions(request):
    city_id = request.GET.get('city_id')
    competitions = Competition.objects.filter(city_id=city_id).all()
    return render(request, 'city_dropdown_list_options.html',{'competitions':competitions})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)