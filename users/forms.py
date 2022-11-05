from django import forms

from .models import Person, Competition,City, Team

EXTRA_CHOICES = [
('0', 'Select City'),
]
class PersonCreationForm(forms.ModelForm):
    city=forms.ChoiceField(label='Select City',choices=(),widget=forms.Select(),initial='0')
    def __init__(self, *args, **kwargs):
        super(PersonCreationForm, self).__init__(*args, **kwargs)
        choices = [(city.id, (city)) for city in City.objects.filter(comingsoon=False).filter(completionstatus=False).all()]
        print(choices)
        choices.extend(EXTRA_CHOICES)
        choices.reverse()
        self.fields['city'].choices = choices
    
    def clean_city(self):
        city=self.cleaned_data['city']
        return City.objects.get(id=int(city))

    class Meta:
        model = Person
        fields = ['name', 'countrycode', 'contactno', 'email', 'college_name', 'city', 'yearofgraduation']


class EntryForm(forms.ModelForm):
    # city=forms.ModelMultipleChoiceField(widget=forms.Select(),queryset=City.objects.filter(comingsoon=False).all())

    city=forms.ChoiceField(label='Select City',choices=(),widget=forms.Select(),initial='0')
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        choices = [(city.id, (city)) for city in City.objects.filter(comingsoon=False).filter(completionstatus=False).all()]
        choices.extend(EXTRA_CHOICES)
        choices.reverse()
        self.fields['city'].choices = choices

    def clean_city(self):
        city=self.cleaned_data['city']
        return City.objects.get(id=int(city))

    class Meta:
        model = Person
        fields = ['competition','city']


class EntryFormTeams(forms.ModelForm):
    # city=forms.ModelMultipleChoiceField(widget=forms.Select(),queryset=City.objects.filter(comingsoon=False).all())
    city=forms.ChoiceField(label='Select City',choices=(),widget=forms.Select(),initial='0')
    def __init__(self, *args, **kwargs):
        super(EntryFormTeams, self).__init__(*args, **kwargs)
        choices = [(city.id, (city)) for city in City.objects.filter(comingsoon=False).filter(completionstatus=False).all()]
        choices.extend(EXTRA_CHOICES)
        choices.reverse()
        self.fields['city'].choices = choices

    def clean_city(self):
        city=self.cleaned_data['city']
        return City.objects.get(id=int(city))
    class Meta:
        model = Team
        # fields = "__all__"
        fields = ['name','members','competition','city']