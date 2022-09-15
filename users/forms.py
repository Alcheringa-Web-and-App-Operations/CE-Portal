from django import forms

from .models import Person, Competition,City,Team


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class EntryForm(forms.ModelForm):
  
    class Meta:
        model = Person
        fields = ['competition','city',]

class EntryForm_teams(forms.ModelForm):
  
    class Meta:
        model = Team
        fields = '__all__'
