from django import forms

from .models import Person, Competition,City


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class EntryForm(forms.ModelForm):
  
    class Meta:
        model = Person
        fields = ['competition','city']
