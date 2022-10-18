from django import forms

from .models import Person, Competition,City, Team

class PersonCreationForm(forms.ModelForm):
    city=forms.ModelMultipleChoiceField(widget=forms.Select(),queryset=City.objects.filter(comingsoon=False).all())
    class Meta:
        model = Person
        fields = ['name', 'countrycode', 'contactno', 'email', 'college_name', 'city', 'yearofgraduation']


class EntryForm(forms.ModelForm):
    city=forms.ModelMultipleChoiceField(widget=forms.Select(),queryset=City.objects.filter(comingsoon=False).all())
    class Meta:
        model = Person
        fields = ['competition','city']


class EntryFormTeams(forms.ModelForm):
    city=forms.ModelMultipleChoiceField(widget=forms.Select(),queryset=City.objects.filter(comingsoon=False).all())
    class Meta:
        model = Team
        # fields = "__all__"
        fields = ['name','members','competition','city']