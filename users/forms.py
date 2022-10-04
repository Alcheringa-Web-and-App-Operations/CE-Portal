from django import forms

from .models import Person, Competition,City, Team


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'countrycode', 'contactno', 'email', 'college_name', 'city', 'yearofgraduation']

class EntryForm(forms.ModelForm):
  
    class Meta:
        model = Person
        fields = ['competition','city']


class EntryFormTeams(forms.ModelForm):

    class Meta:
        model = Team
        # fields = "__all__"
        fields = ['name','members','competition','city']